def insertion(array):
    if array[0] > array[1]:
        tmp = array[0]
        array[0] = array[1]
        array[1] = tmp
    for i in range(2, len(array)):
        tmp = array[i]
        for j in range(i-1, -1, -1):
            if tmp < array[j]:
                array[j+1] = array[j]
                array[j] = tmp
    return array


if __name__ == '__main__':
    length = input()
    array = [int(i) for i in input().split()]
    rez = insertion(array)
    rez_txt = ' '.join(map(str, rez))
    print(rez_txt)