def solution(num, open_br, close_br, string):
    if (open_br + close_br) == (2 * num):
        print(string)
        return

    if open_br < num:
        solution(num, open_br + 1, close_br, string + '(')
    if open_br > close_br:
        solution(num, open_br, close_br + 1, string + ')')


if __name__ == "__main__":
    num = int(input())
    solution(num, 0, 0, '')
