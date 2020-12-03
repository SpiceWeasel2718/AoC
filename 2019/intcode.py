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