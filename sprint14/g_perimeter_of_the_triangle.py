def triangle(array):
    array.sort()
    perimeter = False

    while perimeter == False:
        if array[-1] < array[-2] + array[-3]:
            perimeter = array[-1] + array[-2] + array[-3]
        else:
            array.pop(-1)
    return perimeter


if __name__ == '__main__':
    n = input()
    array = [int(i) for i in input().split()]
    rez = triangle(array)
    print(rez)
