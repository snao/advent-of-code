def pair_checker(letters):
    if abs(ord(letters[0]) - ord(letters[1])) == 32:
        return 1
    else:
        return 0


if __name__ == "__main__":
    with open("day5_input.txt") as f:
        orig_text = f.read()
    i = 0
    alpha_list = []

    for i in range(0, 26):
        text = orig_text
        text = text.replace(chr(i+65), "")
        text = text.replace(chr(i+97), "")
        while i != len(text) - 1:
            current_text = text[i:i+2]
            i += 1
            if pair_checker(current_text):
                text = text.replace(current_text, "")
                i = 0
        alpha_list.append(len(text))

    print(min(alpha_list))
    alpha_index = alpha_list.index(min(alpha_list))
    print(chr(alpha_index+65))
