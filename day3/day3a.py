import re
import numpy as np


def claim_process(line):
    line = re.split('[ ,x]', line)
    del line[0:2]
    line[1] = line[1][:-1]
    coords = [int(x) for x in line]
    return coords


def fabric_chope(array, coords):
    x = coords[0]
    y = coords[1]
    width = coords[2]
    height = coords[3]
    array[y: y + height, x: x + width] += 1
    return array


def check_chope(array, coords):
    x = coords[0]
    y = coords[1]
    width = coords[2]
    height = coords[3]
    if np.all(array[y: y + height, x: x + width] == 1):
        return 1
    else:
        return 0


if __name__ == "__main__":
    with open("day3.txt") as f:
        inp = f.read().strip().splitlines()
    fabric = np.zeros((1000, 1000))
    for line in inp:
        coords = claim_process(line)
        fabric = fabric_chope(fabric, coords)
    more_than_1 = fabric > 1
    print(sum(sum(more_than_1)))

