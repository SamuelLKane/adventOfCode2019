testInput = [1, 0, 0, 0, 99]
pwd = "/Users/samuelkane/Documents/Development/adventOfCode2019/day2/"
with open(pwd + 'input.data') as fh:
    program = [int(value) for value in fh.read().split(',')]
    post = []
    buffer = []
    print(program)
    for i in range(len(program)):
        # fill the buffer until we reach a halt or have a full line to execute
        halt = True if program[i] == 99 else False
        if(not halt and len(buffer) <= 3):
            buffer.append(program[i])
            continue
        if(halt):
            break  # we have reached the end of the program
        print(buffer)
        post = post + buffer
        addMult = buffer[0]
        if (addMult != 1 and addMult != 2):
            raise Exception(f"Invalid addMult key - {addMult} | Buffer {buffer}".rstrip())
        index1 = buffer[1]
        if (index1 > len(program) or index1 < 0):
            raise Exception(f"Invalid index1 key - {index1} | Buffer {buffer}".rstrip())
        index2 = buffer[2]
        if (index2 > len(program) or index2 < 0):
            raise Exception(f"Invalid index2 key - {index2} | Buffer {buffer}".rstrip())
        dest = buffer[3]
        if (dest > len(program) or dest < 0):
            raise Exception(f"Invalid dest key - {dest} | Buffer {buffer}".rstrip())

        if(addMult == 1):
            print(f"{program[index1]} + {program[index2]} into index {dest}")
            program[dest] = program[index1] + program[index2]
        else:
            print(f"{program[index1]} * {program[index2]} into index {dest}")
            program[dest] = program[index1] * program[index2]

        buffer = []
        buffer.append(program[i])

    print(program)
    print(post)
