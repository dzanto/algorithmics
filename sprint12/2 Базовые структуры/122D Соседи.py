ny = int(input())
mx = int(input())

matrix = []
for i in range(ny):
    matrix.append(list(map(int, input().split())))
# print(matrix)

y = int(input())
x = int(input())

neighbours = [[], [], [], []]

neighbours[0].append(y - 1)
neighbours[0].append(x)
neighbours[1].append(y)
neighbours[1].append(x + 1)
neighbours[2].append(y + 1)
neighbours[2].append(x)
neighbours[3].append(y)
neighbours[3].append(x - 1)

# print(neighbours)

result = []
for i in neighbours:
    if i[0] in range(ny) and i[1] in range(mx):
        result.append(matrix[i[0]][i[1]])
# print(result)
result.sort()
# print(result)
print(' '.join(map(str, result)))
