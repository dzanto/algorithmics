x = list(input())[::-1]
y = list(input())[::-1]
if x >= y:
    big = x
    small = y
else:
    big = y
    small = x
len_small = len(small)
for i in small:
    sum = i + big[i]
    if i + big[i] == 2:


