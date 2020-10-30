import math

def solution(element):
    if element == 1:
        return print(0)
    elif element == 2:
        return print(1)
    k = int(math.sqrt(element)) + 1
    mid = 2 ** (k-1)

    if element > mid:
        element = element - mid
        row = [1, 0]
    else:
        row = [0, 1]

    while len(row) < element:
        second_row = [0 if i == 1 else 1 for i in row]
        row.extend(second_row)
    print(row[element-1])



if __name__ == "__main__":
    row = input()
    element = int(input())
    solution(element)
