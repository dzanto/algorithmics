def quicksort(array):
    if len(array) < 2:
        return array  # базовый случай: массивы с 0 и 1 элементом уже отсортированы

    else:
        pivot = array[0]  # рекурсивный случай
        less = [i for i in array[1:] if i <= pivot]  # подмассив всех элементов, меньших опорного
        greater = [i for i in array[1:] if i > pivot]  # подмассив всех элементов, больших опорного
        return quicksort(less) + [pivot] + quicksort(greater)


if __name__ == '__main__':
    n = input()
    array = [int(i) for i in input().split()]
    rez = quicksort(array)
    print(' '.join(map(str, rez)))
