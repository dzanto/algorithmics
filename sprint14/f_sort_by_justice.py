def quicksort(array):
    for i in range(len(array)-1):
        tmp = array[i]
        print(array[i] % 2, i % 2)
        if array[i] % 2 == 0 and (i % 2 == 0 or i == 0):
            continue
        elif array[i] % 2 == 1 and i % 2 == 1:
            continue
        elif array[i] % 2 == 1 and i % 2 == 1:
            print(1, i)
            for j in range(i+1, len(array)-1):
                if array[j] % 2 == 1:
                    continue
                else:
                    array[i] = array[j]
                    array[j] = tmp
                    break
        elif array[i] % 2 == 0 and i % 2 == 0:
            print(2, i)
            for j in range(i + 1, len(array) - 1):
                if array[j] % 2 == 0:
                    continue
                else:
                    array[i] = array[j]
                    array[j] = tmp
    return array


if __name__ == '__main__':
    n = input()
    array = [int(i) for i in input().split()]
    rez = quicksort(array)
    print(' '.join(map(str, rez)))