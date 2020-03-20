import pytest
from find_intersection import findMinimumDistanceForWireIntersection

# Using test values provided by question
def test_wire_path_intersection_and_distance_logic():
    centralPort = (0, 0)
    assert findMinimumDistanceForWireIntersection(centralPort,
        ['R8', 'U5', 'L5', 'D3'],
        ['U7', 'R6', 'D4', 'L4']) == 6
    assert findMinimumDistanceForWireIntersection(centralPort,
        ['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'],
        ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']) == 159
    assert findMinimumDistanceForWireIntersection(centralPort,
        ['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51'],
        ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7']) == 135
