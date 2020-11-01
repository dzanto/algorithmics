n = int(input())
m = int(input())
mat = []
for i in range(n):
    mat.append(list(map(int, input().split())))
# print(mat)
string = []

while mat != []:
    # print(mat[0])
    for i in mat[0]:
        print(i)
    mat.pop(0)

    while [] in mat:
        mat.remove([])
    if mat == []:
        break

    for i in mat:
        print(i[-1])
        i.pop(-1)

    while [] in mat:
        mat.remove([])
    if mat == []:
        break

    rev = mat[-1]
    rev.reverse()
    # print(rev)
    for i in rev:
        print(i)
    mat.pop(-1)
    # print(mat)
    while [] in mat:
        mat.remove([])
    if mat == []:
        break

    # print(mat)
    left = []
    for i in mat:
        if i == []:
            continue
        left.append(i[0])
        i.pop(0)


    left.reverse()
    for i in left:
        print(i)

    while [] in mat:
        mat.remove([])
    if mat == []:
        break
