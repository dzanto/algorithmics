x = int(input())


def stepen(x):
    if x == 1:
        return print(True)
    while x >= 4:
        x = x/4
        if x == 1:
            return print(True)
    if x < 4:
        return print(False)


stepen(x)
