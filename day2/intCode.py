pwd = "/Users/samuelkane/Documents/Development/adventOfCode2019/day2/"
with open(pwd + 'input.data') as fh:
    program = [int(value) for value in fh.read().split(',')]
    print(program)
    for i in range(0, len(program), 4):
        opcode = program[i]
        if opcode == 99:
            break
        index1, index2, dest = program[i+1], program[i+2], program[i+3]
        if opcode == 1:
            program[dest] = program[index1] + program[index2]
        elif opcode == 2:
            program[dest] = program[index1] * program[index2]
        else:
            raise Exception(f"Invalid opcode {opcode}")
    print(program)
