def solution(string):
    for i in range(-1, -len(string), -1):
        if string[i] == ' ':
            return - i - 1
    return len(string)


if __name__ == '__main__':
    string = input()
    print(solution(string))
