def solution(short_string, long_string):
    for i in range(-1, -len(long_string)-1, -1):
        if short_string == []:
            return True
        if long_string[i] == short_string[-1]:
            short_string.pop(-1)
        if short_string == []:
            return True
    return False


if __name__ == '__main__':
    short_string = list(input())
    long_string = list(input())
    print(solution(short_string, long_string))