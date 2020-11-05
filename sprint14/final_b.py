# 39337938
def radix_sort(array):
    # вычисляем максимальное количество разрядов "rank":
    rank = max(map(lambda x: len(x), array))

    # генерируем "пустой" массив списков c нолями:
    zero_array = [
        [0 for _ in range(rank)] for _ in range(len(array))
    ]

    # переносим исходные значения в массив с нолями
    for i in range(len(array)):
        for x in range(-1, -len(array[i])-1, -1):
            current_digit = int(array[i][x])
            zero_array[i][x] = current_digit

    # производим поразрядную сортировку
    for i in range(rank - 1, -1, -1):
        zero_array.sort(key=lambda p: p[i])

    # подготавливаем данные для вывода
    array.clear()
    for i in range(len(zero_array)):
        array.append([])
        end_number = False
        # проходим по каждому числу
        for x in range(rank):
            # пропускаем ноли спереди числа
            # или ждем последнюю цифру в числе
            if (
                    zero_array[i][x] == 0
                    and end_number is False
                    and x != (rank - 1)
            ):
                continue
            # добавляем оставшиейся цифры в пустой массив
            else:
                end_number = True
                array[i].append(str(zero_array[i][x]))
        # склеиваем списки в строки
        array[i] = ''.join(array[i])
    print(' '.join(array))


if __name__ == '__main__':
    n = input()
    del n
    array = [list(i) for i in input().split()]
    radix_sort(array)
