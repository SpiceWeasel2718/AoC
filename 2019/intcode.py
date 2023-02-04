import collections
import threading

class IntComp:
    def __init__(self, program=None, input_values=None):
        self.input_deque = collections.deque()
        self.outputs = []  # internal record of the outputs; different from output_receiver
        self.pos = 0
        self.rel_base = 0
        self.halted = False
        
        self.output_receiver = None  # another IntComp that gets the outputs from this one
        self.output_event = threading.Event()
        self.output_event.set()
        self.input_provider = None  # another IntComp that provides the inputs for this one
        self.input_event = threading.Event()
        self.input_event.set()
        self.waiting_on_input = threading.Event()  # set when waiting on input, cleared when input is received
        self.event_timeout = 2

        if program:
            self.set_program(program)
        if input_values:
            self.append_inputs(input_values)

    def reset(self):
        self.program = self.original_program.copy()
        self.pos = 0
        self.rel_base = 0
        self.outputs.clear()
        self.input_deque.clear()
        self.halted = False

    def set_program(self, program):
        try:
            parsed_program = [int(c) for c in program.split(',')]
        except AttributeError:
            parsed_program = program
        self.program = collections.defaultdict(int, enumerate(parsed_program))
        self.original_program = self.program.copy()

    def append_inputs(self, input_values):
        try:
            self.input_deque.extend(input_values)
        except TypeError:
            self.input_deque.append(input_values)
        self.input_event.set()
        self.waiting_on_input.clear()

    def halt(self):
        self.halted = True
        self.input_event.set()
        self.waiting_on_input.set()
        return self.outputs

    def set_output_receiver(self, output_receiver):
        self.output_receiver = output_receiver

    def set_input_provider(self, input_provider):
        self.input_provider = input_provider

    def set_event_timeout(self, timeout):
        self.event_timeout = timeout

    OPCODE_NPARAMS = {
        1: 3, 
        2: 3, 
        3: 1, 
        4: 1, 
        5: 2, 
        6: 2, 
        7: 3, 
        8: 3, 
        9: 1,
        99: 0
    }

    def execute(self):
        while not self.halted:
            instruction = self.program[self.pos]
            opcode = instruction % 100
            mode_indicator = instruction // 100
            param_pointers = []
            first_param = self.pos + 1
            
            for i in range(self.OPCODE_NPARAMS[opcode]):
                mode = mode_indicator % 10
                mode_indicator //= 10
                
                if mode == 0:
                    param_pointers.append(self.program[first_param + i])
                elif mode == 1:
                    param_pointers.append(first_param + i)
                elif mode == 2:
                    param_pointers.append(self.program[first_param + i] + self.rel_base)
                else:
                    raise Exception(f'Error: unknown mode {mode}')

            if opcode == 1:  # add
                p1, p2, out = param_pointers
                self.program[out] = self.program[p1] + self.program[p2]

            elif opcode == 2:  # multiply
                p1, p2, out = param_pointers
                self.program[out] = self.program[p1] * self.program[p2]

            elif opcode == 3:  # input
                if self.input_provider:
                    # allow the provider to provide input
                    # if you need to control input rate from providers, do it here
                    self.input_provider.output_event.set()

                try:
                    self.program[param_pointers[0]] = self.input_deque.popleft()
                except IndexError:
                    # if input_deque is empty, wait until it isn't
                    self.input_event.clear()
                    self.waiting_on_input.set()  # indicates all outputs before this input are complete
                    self.input_event.wait(timeout=self.event_timeout)
                    if not self.halted:
                        self.program[param_pointers[0]] = self.input_deque.popleft()

            elif opcode == 4:  # output
                output = self.program[param_pointers[0]]

                if self.output_receiver:
                    # wait to provide input until allowed by receiver
                    self.output_event.wait(timeout=self.event_timeout)
                    self.output_receiver.append_inputs(output)
                
                self.outputs.append(output)

            elif opcode == 5:  # jump-if-true
                check, jump = param_pointers
                if self.program[check]:
                    self.pos = self.program[jump]
                    continue

            elif opcode == 6:  # jump-if-false
                check, jump = param_pointers
                if not self.program[check]:
                    self.pos = self.program[jump]
                    continue

            elif opcode == 7:  # less than
                p1, p2, out = param_pointers
                self.program[out] = (self.program[p1] < self.program[p2])

            elif opcode == 8:  # equals
                p1, p2, out = param_pointers
                self.program[out] = (self.program[p1] == self.program[p2])

            elif opcode == 9:  # relative base offset
                self.rel_base += self.program[param_pointers[0]]

            elif opcode == 99:  # halt
                self.halted = True
                self.waiting_on_input.set()  # lets anything waiting on this to proceed
                return self.outputs
            
            self.pos += self.OPCODE_NPARAMS[opcode] + 1


# import collections
import asyncio

class IntcodeComputer:
    def __init__(self, init_state=None):
        self.state = collections.defaultdict(int)
        self.init_state = init_state
        self.pos_pointer = 0
        self.rel_base = 0
        self.input_queue = asyncio.Queue()
        self.output_queue = asyncio.Queue()
        
    def load_program(self, intcode_string):
        for k, v in enumerate(intcode_string.split(',')):
            self.state[k] = int(v)
        self.init_state = self.state.copy()
    
    def set_input_queue(self, input_queue):
        self.input_queue = input_queue
    
    def set_output_queue(self, output_queue):
        self.output_queue = output_queue
    
    OPCODE_NPARAMS = {
        1: 3, 
        2: 3, 
        3: 1, 
        4: 1, 
        5: 2, 
        6: 2, 
        7: 3, 
        8: 3, 
        9: 1,
        99: 0
    }

    async def run(self):
        while True:
            param_modes, opcode = divmod(self.state[self.pos_pointer], 100)

            param_pointers = []

            for i in range(self.pos_pointer + 1, self.pos_pointer + self.OPCODE_NPARAMS[opcode] + 1):
                param_modes, mode = divmod(param_modes, 10)

                if mode == 0:  # position
                    param_pointers.append(self.state[i])
                elif mode == 1:  # immediate
                    param_pointers.append(i)
                elif mode == 2:  # relative
                    param_pointers.append(self.state[i] + self.rel_base)

            if opcode == 1:  # add
                p1, p2, p3 = param_pointers
                self.state[p3] = self.state[p1] + self.state[p2]
            elif opcode == 2:  # multiply
                p1, p2, p3 = param_pointers
                self.state[p3] = self.state[p1] * self.state[p2]
            elif opcode == 3:  # input
                self.state[param_pointers[0]] = await self.input_queue.get()
            elif opcode == 4:  # output
                await self.output_queue.put(self.state[param_pointers[0]])
            elif opcode == 5:  # jump-if-true
                if self.state[param_pointers[0]]:
                    self.pos_pointer = self.state[param_pointers[1]] - self.OPCODE_NPARAMS[opcode] - 1
            elif opcode == 6:  # jump-if-false
                if not self.state[param_pointers[0]]:
                    self.pos_pointer = self.state[param_pointers[1]] - self.OPCODE_NPARAMS[opcode] - 1
            elif opcode == 7:  # less than
                p1, p2, p3 = param_pointers
                self.state[p3] = (self.state[p1] < self.state[p2])
            elif opcode == 8:  # equals
                p1, p2, p3 = param_pointers
                self.state[p3] = (self.state[p1] == self.state[p2])
            elif opcode == 9:  # adjust relative base
                self.rel_base += self.state[param_pointers[0]]
            elif opcode == 99:
                return

            self.pos_pointer += self.OPCODE_NPARAMS[opcode] + 1


if __name__ == "__main__":
    with open("input_files/AoC2019_day05_input.txt") as f:
        program = f.read().strip()
    
    ic = IntcodeComputer()
    ic.load_program(program)
    ic.input_queue.put_nowait(5)
    asyncio.run(ic.run())
    print(ic.output_queue)