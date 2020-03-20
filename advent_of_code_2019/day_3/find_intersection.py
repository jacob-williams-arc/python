increment = {'R': (1, 0),
             'L': (-1, 0),
             'U': (0, 1),
             'D': (0, -1)}


def followPath(currentPosition, direction):
    return [sum(x) for x in zip(currentPosition, increment[direction])]


def buildWirePath(startingPosition, moves):
    path = set()
    currentPosition = startingPosition
    for move in moves:
        direction, distance = move[0], int(move[1:])
        while distance > 0:
            currentPosition = followPath(currentPosition, direction)
            path.add(tuple(currentPosition))
            distance -= 1

    return path


def findIntersections(pathA, pathB):
    return pathA.intersection(pathB)


def findManhattanDistances(intersectionPoints):
    return [sum([abs(x), abs(y)]) for [x, y] in intersectionPoints]


def findMinimumDistanceForWireIntersection(centralPort, wirePathA, wirePathB):
    return min(findManhattanDistances(findIntersections(
        buildWirePath(centralPort, wirePathA),
        buildWirePath(centralPort, wirePathB))))


def loadAndProcess(filename):
    centralPort = (0, 0)
    with open(filename) as inputFile:
        paths = inputFile.readlines()

    return findMinimumDistanceForWireIntersection(
        centralPort,
        paths[0].split(','),
        paths[1].split(','))

print(loadAndProcess('./wire_paths'))
