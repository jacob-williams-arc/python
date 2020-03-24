increment = {'R': (1, 0),
             'L': (-1, 0),
             'U': (0, 1),
             'D': (0, -1)}


def followPath(currentPosition, direction):
    return [sum(x) for x in zip(currentPosition, increment[direction])]


def buildWirePath(startingPosition, moves):
    path = []
    currentPosition = startingPosition
    for move in moves:
        direction, distance = move[0], int(move[1:])
        while distance > 0:
            currentPosition = followPath(currentPosition, direction)
            path.append(tuple(currentPosition))
            distance -= 1

    return path


def findIntersections(pathA, pathB):
    return set(pathA) & set(pathB)


def findManhattanDistances(intersectionPoints):
    return [sum([abs(x), abs(y)]) for [x, y] in intersectionPoints]


def findMinimumDistanceForWireIntersection(centralPort, wirePathA, wirePathB):
    return min(findManhattanDistances(findIntersections(
        buildWirePath(centralPort, wirePathA),
        buildWirePath(centralPort, wirePathB))))


def findMinimumDistanceToIntersectionPoints(pathA, pathB):
    intersectionPoints = findIntersections(pathA, pathB)

    return min([(pathA.index(x) + 1)
                + (pathB.index(x) + 1) for x in intersectionPoints])


def loadData(filename):
    with open(filename) as inputFile:
        paths = inputFile.readlines()

    return paths


def loadAndProcessPart1(centralPort, filename):
    paths = loadData(filename)

    return findMinimumDistanceForWireIntersection(
        centralPort,
        paths[0].split(','),
        paths[1].split(','))


def loadAndProcessPart2(centralPort, filename):
    paths = loadData(filename)
    pathA = buildWirePath(centralPort, paths[0].split(','))
    pathB = buildWirePath(centralPort, paths[1].split(','))

    return findMinimumDistanceToIntersectionPoints(pathA, pathB)


centralPort = (0, 0)
print(loadAndProcessPart1(centralPort, './wire_paths'))
print(loadAndProcessPart2(centralPort, './wire_paths'))
