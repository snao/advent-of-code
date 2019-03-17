def str_compare(str1, str2):
    diff_letter = 0
    index = 0
    for i in range(0, len(str1)-1):
        if str1[i] != str2[i]:
            diff_letter += 1
            index = i
    if diff_letter == 1:
        return index
    else:
        return 0


def remove_index(s, i):
    return s[:i] + s[i+1:]


if __name__ == "__main__":
    with open("day2.txt") as f:
        inp = f.read().strip().splitlines()
    for i in range(0, len(inp)-2):
        for j in range(i+1, len(inp)-1):
            index = str_compare(inp[i], inp[j])
            if index != 0:
                ans = remove_index(inp[i], index)
                print(ans)
                quit()
