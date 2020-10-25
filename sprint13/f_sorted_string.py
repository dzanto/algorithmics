import string
lowercase = list(string.ascii_lowercase)
DICT_LOW = {lowercase[i]: i for i in range(len(lowercase))}


def del_string(lines):
    count = 0
    for sym in range(len(lines[0])):
        lowercase = list(string.ascii_lowercase)
        for i in lines:
            if i[sym] in lowercase:
                for letter in range(DICT_LOW[i[sym]]):
                    lowercase[letter] = ''
                # print(i[sym], lowercase)
            else:
                count += 1
                break
    return count


if __name__ == "__main__":

    number_of_lines = int(input())
    string_length = int(input())
    lines = []
    for i in range(number_of_lines):
        lines.append(list(input()))
    # print(lines)
    print(del_string(lines))

