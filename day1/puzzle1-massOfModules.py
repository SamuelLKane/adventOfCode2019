import math

with open("puzzle1-input.data") as fh:
    total = 0
    for line in fh.readlines():
        val = math.floor(int(line) / 3) - 2
        total = total + val
    print(total)