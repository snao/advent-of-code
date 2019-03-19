def pair_checker(letters):
    if abs(ord(letters[0]) - ord(letters[1])) == 32:
        return 1
    else:
        return 0


if __name__ == "__main__":
    with open("day5_input.txt") as f:
        text = f.read()
    i = 0

    while i != len(text) - 1:
        current_text = text[i:i+2]
        i += 1
        if pair_checker(current_text):
            text = text.replace(current_text, "")
            i = 0

    print(len(text))
