testInput = [2,3,0,3,99]
pwd = "/Users/samuelkane/Documents/Development/adventOfCode2019/day2/"
with open(pwd + 'input.data') as fh:
    program = [int(value) for value in fh.read().split(',')]
    # program = testInput
    currentBufferIndex = 0
    while(True):
        buffers = [program[i*4:(i+1) * 4] for i in range((len(program) + 3) // 4)]
        print(buffers)
        currentBuffer = buffers[currentBufferIndex]
        if 99 in currentBuffer:
            break  # reached a halt
        addMult = currentBuffer[0]
        index1 = currentBuffer[1]
        index2 = currentBuffer[2]
        dest = currentBuffer[3]
        if addMult == 1:
            print(f"{program[index1]} + {program[index2]} into {dest}")
            program[dest] = program[index1] + program[index2]
        elif addMult == 2:
            print(f"{program[index1]} * {program[index2]} into {dest}")
            program[dest] = program[index1] * program[index2]
        else:
            raise Exception(f"Invalid addMult value {addMult} in buffer {currentBuffer}".rstrip())
        currentBufferIndex = currentBufferIndex + 1
    print(program)
