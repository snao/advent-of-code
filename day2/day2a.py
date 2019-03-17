def parse_1(line):
    chars = [0] * 26
    for letter in line:
        c = ord(letter)
        chars[c-97] += 1
    if 2 in chars:
        return 1
    else:
        return 0


def parse_2(line):
    chars = [0] * 26
    for letter in line:
        c = ord(letter)
        chars[c - 97] += 1
    if 3 in chars:
        return 1
    else:
        return 0


if __name__ == "__main__":
    with open("day2.txt") as f:
        inp = f.read().strip().splitlines()
    twice = 0
    thrice = 0
    for lines in inp:
        twice += parse_1(lines)
        thrice += parse_2(lines)
    print(twice*thrice)
