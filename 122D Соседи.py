n = 3
m = 3
x = 1
y = 1
matrix = []
for i in range(n):
    matrix.append(list(input().split()))
print(matrix)

# CALC = {
#     '+x': (lambda x, y: ),
#     '-x':,
#     '+y':,
#     '-y':,
# }
position = [[], [], [], []]

position[0][0] = y+1
position[0][1] = x
position[1][0] = y-1
position[1][1] = x
position[2][0] = y
position[2][1] = x+1
position[3][0] = y
position[3][1] = x-1

for y in
