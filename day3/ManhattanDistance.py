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
        if manDist < shortestCord:
            shortestCord = manDist
    return shortestCord


pwd = "/Users/samuelkane/Documents/Development/adventOfCode2019/day3/"
wireDirections = [line.strip().split(',') for line in open(pwd + "input.data").readlines()]
# wireDirections = [['R8','U5','L5','D3'],['U7','R6','D4','L4']]

wire0Coords = buildWireCoords(wireDirections[0])
wire1Coords = buildWireCoords(wireDirections[1])

wire0Coords.sort(key=manhattanSort)
wire1Coords.sort(key=manhattanSort)
commonCords = []

for wire0Coord in wire0Coords:
    if wire0Coord in wire1Coords:
        print(wire0Coord)
        commonCords.append(wire0Coord)

shortestDist = findShortestManhattanDistance(commonCords)
print(shortestDist)
