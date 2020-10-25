al = list('abcdefghijklmnopqrstuvwxyz')
# print(al)
# new_al=[]
f = open('input.txt', 'r')
n = f.read()

def alp(n, i):
    if n != al[i]:
        print(al[i], end=' ')
        alp(n, i+1)
    else:
        print(n, end='')


alp(n, 0)
