f = open('input.txt', 'r')
n = int(f.read())
fac = 1
for i in range(n):
    fac = fac * (n)
    n = n - 1
print(fac)
