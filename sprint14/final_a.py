from operator import itemgetter

def solution(array):
    # array = list(map(list, array))
    # print(array)
    for a in range(len(array)):
        for b in range(len(array)-1):
            right = int(array[b] + array[b + 1])
            revers = int(array[b + 1] + array[b])
            if right < revers:
                array[b], array[b + 1] = array[b + 1], array[b]
    for i in array:
        print(i, end='')



    # new_array = []
    # for i in range(len(array)):
    #     new_array.append([])
    #     for x in array[i]:
    #         x = int(x)
    #         new_array[i].append(x)
    #     while len(new_array[i]) < 4:
    #         new_array[i].append(10)
    #
    # new_array.sort(reverse=True, key=itemgetter(0, 1, 2, 3))
    # print(new_array)
    # for i in new_array:
    #     for x in i:
    #         if x < 10:
    #             print(x, end='')
    #         else:
    #             break
    #     print(' ')
    # zero = [[], [], [], []]

    # for i in array:
    #     if i <= 9:
    #         zero[0].append(i)
    #     elif i <= 99:
    #         zero[1].append(i)
    #     elif i <= 999:
    #         zero[2].append(i)
    #     else:
    #         zero[3].append(i)
    # for i in zero:
    #     i.sort(reverse=True)
    #     for x in i:
    #         print(x, end='')


if __name__ == '__main__':
    n = input()
    array = [i for i in input().split()]
    solution(array)
