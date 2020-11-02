import math

# def solution(element):
#     if element == 1:
#         return print(0)
#     elif element == 2:
#         return print(1)
#     k = int(math.sqrt(element)) + 1
#     mid = 2 ** (k-1)
#
#     if element > mid:
#         element = element - mid
#         row = [1, 0]
#     else:
#         row = [0, 1]
#
#     while len(row) < element:
#         second_row = [0 if i == 1 else 1 for i in row]
#         row.extend(second_row)
#     print(row[element-1])

dic_row = {
    0: [0, 1, 1, 0],
    1: [1, 0, 0, 1]
}


def change_sw(sw):
    if sw == 0:
        sw = 1
    else:
        sw = 0
    return sw


def solution(key, sw):
    # print('key=', key, 'sw=', sw)
    if key <= 4:
        return print(dic_row[sw][key - 1])

    tmp = key
    step = 0
    while tmp >= 2:
        tmp = tmp / 2
        step += 1
    # print('step=', step)
    mid = 2 ** step

    if key == mid:
        if step % 2 == 0:
            return print(sw)
        else:
            return print(change_sw(sw))

    new_key = key - mid
    sw = change_sw(sw)
    solution(new_key, sw)


if __name__ == "__main__":
    row = input()
    element = int(input())
    solution(element, sw=0)
