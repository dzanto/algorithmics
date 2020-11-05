def quicksort(array):

    for i in range(len(array)-1):
        tmp = array[i]
        # print(tmp, array[i] % 2, i % 2)
        # print(array)
        if array[i] % 2 == 0 and (i % 2 == 0 or i == 0):
            continue
        elif array[i] % 2 == 1 and i % 2 == 1:
            continue
        elif array[i] % 2 == 1 and i % 2 == 0:
            for j in range(i, len(array)):
                if array[j] % 2 == 1:
                    tmpa = array[j]
                    array[j] = tmp
                    tmp = tmpa
                else:
                    array[i] = array[j]
                    array[j] = tmp
                    break
        elif array[i] % 2 == 0 and i % 2 == 1:
            for j in range(i, len(array)):
                if array[j] % 2 == 0:
                    tmpa = array[j]
                    array[j] = tmp
                    tmp = tmpa
                else:
                    array[i] = array[j]
                    array[j] = tmp
                    break
    return array


if __name__ == '__main__':
    n = input()
    if n == '0' or '':
        print('')
    else:
        inp = input()
        if inp == '0' or '':
            print(inp)
        else:
            array = [int(i) for i in inp.split()]
            rez = quicksort(array)
            print(' '.join(map(str, rez)))
