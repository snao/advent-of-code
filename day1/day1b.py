def day1a_parse(inp):
    inp = inp.strip().splitlines()
    inp = [int(x) for x in inp]
    return inp


def day1b_twice(inp):
    current_freq = 0
    found = 0
    old_freqs = set()
    while ~found:
        for i in inp:
            if current_freq in old_freqs:
                found = 1
                return current_freq
            else:
                old_freqs.add(current_freq)
                current_freq += i


if __name__ == "__main__":
    with open("day1a_input.txt") as f:
        inp = f.read()
    list = day1a_parse(inp)
    ans = day1b_twice(list)
    print(ans)
