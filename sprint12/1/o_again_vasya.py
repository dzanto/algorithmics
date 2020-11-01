def solution(short, cnt_short, cnt_long, long):
    cnt_short -= 1
    cnt_long -= 1
    for i in range(-1, -len(long)-1, -1):
        if long[cnt_long] <= short[-1]:
            long[i] = short.pop(-1)
        elif cnt_long < 0 and short != []:
            long[i] = short.pop(-1)
        else:
            long[i] = long[cnt_long]
            cnt_long -= 1
        if short == []:
            return long
    return long


if __name__ == '__main__':
    long = [int(i) for i in input().split()]
    cnt_long = int(input())
    cnt_short = int(input())
    short = [int(i) for i in input().split()]
    rezult = solution(short, cnt_short, cnt_long, long)
    rezult = map(str, rezult)
    print(' '.join(rezult))
