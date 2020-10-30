def solution(element):
    row = [0, 1]
    while len(row) < element:
        second_row = [0 if i == 1 else 1 for i in row]
        row.extend(second_row)
    print(row[element-1])


if __name__ == "__main__":
    row = input()
    element = int(input())
    solution(element)
