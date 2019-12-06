# manhattan Distance
def buildWireCoords(directions):
    coords = []
    currentCoord = (0, 0)
    for direction in directions:
        orientation = direction[:1]
        magnitude = int(direction[1:])
        for step in range(magnitude):
            if orientation == 'U':
                currentCoord = (currentCoord[0], currentCoord[1] + 1)
                coords.append(currentCoord[:])
            elif orientation == 'D':
                currentCoord = (currentCoord[0], currentCoord[1] - 1)
                coords.append(currentCoord[:])
            elif orientation == 'L':
                currentCoord = (currentCoord[0] - 1, currentCoord[1])
                coords.append(currentCoord[:])
            elif orientation == 'R':
                currentCoord = (currentCoord[0] + 1, currentCoord[1])
                coords.append(currentCoord)
            else:
                raise Exception("Invalid orientation")
    return coords


def manhattanDistance(val1, val2):
    return abs(val1) + abs(val2)


def manhattanSort(coord):
    return manhattanDistance(coord[0],coord[1])


def findShortestManhattanDistance(coords):
    shortestCord = 99999
    for coord in coords:
        manDist = manhattanDistance(coord[0], coord[1])
        if manDist + coord[2] < shortestCord:
            shortestCord = manDist + coord[2]
    return shortestCord


pwd = "/Users/samuelkane/Documents/Development/adventOfCode2019/day3/"
wireDirections = [line.strip().split(',') for line in open(pwd + "input.data").readlines()]
# wireDirections = [['R8','U5','L5','D3'],['U7','R6','D4','L4']]

wire0Coords = buildWireCoords(wireDirections[0])
wire1Coords = buildWireCoords(wireDirections[1])

# wire0Coords.sort(key=manhattanSort)
# wire1Coords.sort(key=manhattanSort)
commonCords = []

for i in range(len(wire0Coords)):
    wire0Coord = wire0Coords[i]
    if wire0Coord in wire1Coords:
        print(wire0Coord)
        sumOfIndicies = i + wire1Coords.index(wire0Coord)
        coord = (wire0Coord[0],wire0Coord[1],sumOfIndicies)
        # print(coord)
        commonCords.append(coord)

shortestDist = findShortestManhattanDistance(commonCords)
#605/607 - too low
#7827 too high
print(shortestDist)
