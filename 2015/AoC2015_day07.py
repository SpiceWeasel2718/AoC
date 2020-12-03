f = open("input_files/AoC2015_day07_input.txt")
inputs = f.readlines()
f.close()

inputs.remove("19138 -> b\n")
inputs.append("16076 -> b")

def btwand(params):
    a = int(params[0]) if params[0].isnumeric() else circuit[params[0]]
    b = int(params[1]) if params[1].isnumeric() else circuit[params[1]]
    return a & b

def btwor(params):
    a = int(params[0]) if params[0].isnumeric() else circuit[params[0]]
    b = int(params[1]) if params[1].isnumeric() else circuit[params[1]]
    return a | b

def btwnot(param):
    return ~circuit[param]

def btwlshift(params):
    return circuit[params[0]] << int(params[1])

def btwrshift(params):
    return circuit[params[0]] >> int(params[1])

circuit = {}

while len(inputs) > 0:
    for line in inputs:
        op = line.rstrip().split(" -> ")

        if "AND" in line:
            params = op[0].split(" AND ")
            if all([params[i].isnumeric() or params[i] in circuit.keys() for i in range(2)]):
                inputs.remove(line)
                circuit.update({op[1]: btwand(params)})
        elif "OR" in line:
            params = op[0].split(" OR ")
            if all([params[i].isnumeric() or params[i] in circuit.keys() for i in range(2)]):
                inputs.remove(line)
                circuit.update({op[1]: btwor(params)})
        elif "NOT" in line:
            param = op[0][4:]
            if param in circuit.keys():
                inputs.remove(line)
                circuit.update({op[1]: btwnot(param)})
        elif "LSHIFT" in line:
            params = op[0].split(" LSHIFT ")
            if params[0] in circuit.keys():
                inputs.remove(line)
                circuit.update({op[1]: btwlshift(params)})
        elif "RSHIFT" in line:
            params = op[0].split(" RSHIFT ")
            if params[0] in circuit.keys():
                inputs.remove(line)
                circuit.update({op[1]: btwrshift(params)})
        elif op[0].isnumeric():
            inputs.remove(line)
            circuit.update({op[1]: int(op[0])})
        elif op[0] in circuit.keys():
            inputs.remove(line)
            circuit.update({op[1]: circuit[op[0]]})


print("a:", circuit["a"])



