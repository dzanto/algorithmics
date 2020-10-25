f = open('input.txt', 'r')
n = int(f.read())


def factor(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factor(n-1)


print(factor(3)/(factor(3)*(factor(9-3))))
