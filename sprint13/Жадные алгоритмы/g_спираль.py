n = int(input())
m = int(input())
mat = []
if n > m:
    maxim = n
else:
    maxim = m
x = 0
for i in range(n):
    mat.append(list(map(int, input().split())))
# print(mat)
string = []


def spin(v):
    # up
    # print('up=',end='')
    for i in range(m - x):
        # print('up=',end='')
        # print('v=', v)
        # print('i=', i)
        # print(mat[v][i + v], end=' ')
        string.append(mat[v][i + v])
    # right
    # print('right=',end='')
    for i in range(v + 1, n - v):
        # print('right=',end='')
        # print(mat[i][-v-1], end=' ')
        string.append(mat[i][-v - 1])
    # down

    # print('down=',end='')
    if v == 0:
        return string
    for i in range(v + 1, m - v):
        # print('down=',end='')
        # print(mat[-v-1][-i-1], end=' ')
        string.append(mat[-v - 1][-i - 1])
    # left
    # print('left=',end='')
    for i in range(v + 1, n - (v + 1)):
        # print('left=', end='')
        # print(mat[-i-1][v], end=' ')
        string.append(mat[-i - 1][v])



for v in range(2):
    # print('v=', v)
    spin(v)
    x += 2

for i in range(len(string)-1):
    print(string[i])







