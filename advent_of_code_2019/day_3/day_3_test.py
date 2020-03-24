from find_intersection import findMinimumDistanceForWireIntersection
from find_intersection import findMinimumDistanceToIntersectionPoints
from find_intersection import buildWirePath

centralPort = (0, 0)


# Using test values provided by question
def test_case_a():
    assert findMinimumDistanceForWireIntersection(centralPort,
        ['R8', 'U5', 'L5', 'D3'],
        ['U7', 'R6', 'D4', 'L4']) == 6


def test_case_b():
    assert findMinimumDistanceForWireIntersection(centralPort,
        ['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'],
        ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']) == 159


def test_case_c():
    assert findMinimumDistanceForWireIntersection(centralPort,
        ['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51'],
        ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7']) == 135


def test_case_d():
    pathA = buildWirePath(centralPort,
        ['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'])
    pathB = buildWirePath(centralPort,
        ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83'])

    assert findMinimumDistanceToIntersectionPoints(pathA, pathB) == 610


def test_case_e():
    pathA = buildWirePath(centralPort,
        ['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51'])
    pathB = buildWirePath(centralPort,
        ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7'])

    assert findMinimumDistanceToIntersectionPoints(pathA, pathB) == 410
