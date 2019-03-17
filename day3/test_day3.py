from day3a import *
from day3b import *

def test_claim_process():
    ans = claim_process("#123 @ 3,2: 5x4")
    assert ans == [3, 2, 5, 4]


def test_fabric_chope():
    empty_array = np.zeros((3, 3))
    coords = [1, 0, 1, 2]
    ans = fabric_chope(empty_array, coords)
    assert ans == np.array([[0, 1, 0], [0, 1, 0], [0, 0, 0]])


def test_check_chope():
    test_array = np.array([[2, 1, 2], [2, 1, 2], [2, 0, 2]])
    coords = [1, 0, 1, 2]
    ans = check_chope(test_array, coords)
    assert ans == 1