def runProgram(index1Input, index2Input, program):
    program[1] = index1Input
    program[2] = index2Input
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
    return(program[0])


pwd = "/Users/samuelkane/Documents/Development/adventOfCode2019/day2/"
with open(pwd + 'input.data') as fh:
    program = [int(value) for value in fh.read().split(',')]
    print(program)
    for i1 in range(100):
        for i2 in range(100):
            result = runProgram(i1, i2, program[:])
            if result == 19690720:
                print(i1, i2)
