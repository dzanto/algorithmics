# 39485470


def radix_sort(array):
    length = len(str(max(array)))
    rang = 10
    for i in range(length):
        b = [[] for k in range(rang)]
        for x in array:
            digit = x // 10 ** i % 10
            b[digit].append(x)
        array = []
        for k in range(rang):
            array += b[k]
    return array


if __name__ == '__main__':
    input()
    array = [int(i) for i in input().split()]
    sorted_array = radix_sort(array)
    print(' '.join(map(str, sorted_array)))
