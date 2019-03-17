def day1a_parse(inp):
    inp = inp.strip().splitlines()
    inp = [int(x) for x in inp]
    return inp


def day1a_calculate(inp):
    sum = 0
    for i in inp:
        sum += i
    return sum


if __name__ == "__main__":
    with open("day1a_input.txt") as f:
        inp = f.read()
    parsed_input = day1a_parse(inp)
    total = day1a_calculate(parsed_input)
    print(total)
