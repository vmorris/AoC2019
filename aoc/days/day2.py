from itertools import permutations


def execute(opcode, code):
    if opcode[0] == 1:
        value = code[opcode[1]] + code[opcode[2]]
    elif opcode[0] == 2:
        value = code[opcode[1]] * code[opcode[2]]
    code[opcode[3]] = value


def day2(data):
    with open(data, 'r') as f:
        code = list(map(int, f.read().rstrip().split(',')))
    
    inputs = range(100)
    combos = permutations(inputs, r=2)
    
    for noun, verb in combos:
        machine = code.copy()
        machine[1] = noun
        machine[2] = verb
        i = 0
        step = 4
        while i < len(machine):
            opcode = machine[i:i+step]
            if opcode[0] == 99:
                break
            execute(opcode, machine)
            i += step
        if machine[0] == 19690720:
            print(100 * noun + verb)
   