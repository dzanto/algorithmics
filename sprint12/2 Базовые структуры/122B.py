n = int(input())
m = int(input())
a = []
for i in range(n):
    string = list(map(str, input().split()))
    a.append(string)
x = []
for i_m in range(m):
    x.append([])
    for i_n in range(n):
        x[i_m].append(a[i_n][i_m])
for i in x:
    print(' '.join(i))
