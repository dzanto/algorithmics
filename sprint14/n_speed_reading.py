# def quicksort(array):
#     if len(array) < 2:
#         return array # базовый случай: массивы с 0 и 1 элементом уже отсортированы
#     else:
#         pivot = array[0] #рекурсивный случай
#         less = [i for i in array[1:] if i > pivot] #подмассив всех элементов, меньших опорного
#         greater = [i for i in array[1:] if i <= pivot] #подмассив всех элементов, больших опорного
#     return quicksort(less) + [pivot] + quicksort(greater)


def speed_reading(matrix, y_len, x_len):
    dif = 0
    y = 0
    x = 0
    y_cur = 0

    while y_cur < y_len:
        diag = [matrix[y][y + dif] for y in range(y_cur, y_len) if y + dif < x_len]
        diag.sort(reverse=True)

        while y + dif < x_len and y < y_len:
            matrix[y][y + dif] = diag.pop()
            y += 1

        dif -= 1
        y_cur += 1
        y = y_cur

    dif = 1
    x_cur = 1
    x = x_cur
    y = x - dif

    while x_cur < x_len:
        diag = [matrix[x - dif][x] for x in range(x_cur, x_len) if x - dif < y_len]
        diag.sort(reverse=True)

        while x - dif < y_len and x < x_len:
            matrix[x - dif][x] = diag.pop()
            x += 1

        dif += 1
        x_cur += 1
        x = x_cur

    for i in matrix:
        print(' '.join(map(str, i)))


if __name__ == '__main__':
    y_len = int(input())
    x_len = int(input())
    matrix = []
    for i in range(y_len):
        matrix.append([int(i) for i in input().split()])
    speed_reading(matrix, y_len, x_len)
