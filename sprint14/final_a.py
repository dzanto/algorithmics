# 39329479


class BiggestCompare(str):

    def __new__(cls, word):
        return str.__new__(cls, word)

    def __lt__(self, other):
        right = int(self + other)
        revers = int(other + self)
        return right > revers


def max_number(array):
    sorted_array = sorted(array, key=BiggestCompare)
    print(''.join(sorted_array))


if __name__ == '__main__':
    n = input()
    array = [i for i in input().split()]
    max_number(array)
