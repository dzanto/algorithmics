# 39337938
def radix_sort(array):
    print(array)
    length = len(str(max(array)))
    rang = 10
    for i in range(length):
        b = [[] for k in range(rang)]
    for x in array:
        figure = x // 10 ** i % 10
        b[figure].append(x)
        a = []
        for k in range(rang):
            a = a + b[k]
    print(a)


if __name__ == '__main__':
    n = input()
    del n
    array = [int(i) for i in input().split()]
    radix_sort(array)
