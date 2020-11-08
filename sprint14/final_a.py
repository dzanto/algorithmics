# 39485149


class BiggestCompare(str):

    def __lt__(self, other):
        right = int(self + other)
        revers = int(other + self)
        return right > revers


def max_number(array):
    sorted_array = sorted(array, key=BiggestCompare)
    return sorted_array


if __name__ == '__main__':
    input()
    array = [i for i in input().split()]
    sorted_array = max_number(array)
    print(''.join(sorted_array))
