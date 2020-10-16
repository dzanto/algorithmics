#1010
#1011
# 11
# 11
# 110
x = list(map(int, input()))[::-1]
y = list(map(int, input()))[::-1]
print(x)
print(y)

if len(x) >= len(y):
    big = x
    small = y
else:
    big = y
    small = x
different = len(big) - len(small)
for i in range(different):
    small.append(0)
print(small)
print(big)
inc = 0
summa = []
for i in range(len(small)):
    if small[i] + big[i] + inc == 0:
        inc = 0
        summa.append(0)
    elif small[i] + big[i] + inc == 1:
        inc = 0
        summa.append(1)
    elif small[i] + big[i] + inc == 2:
        inc = 1
        summa.append(0)
    elif small[i] + big[i] + inc == 3:
        inc = 1
        summa.append(1)
    # print(summa[i], end=' ')
if inc == 1:
    summa.append(1)
    # print(summa[len(small)])
space = ''
count = 0
for i in summa[::-1]:
    # if count == len(summa)-1:
    #     space = ''
    # count = count + 1
    print(i, end=space)

