import sys
sys.setrecursionlimit(10000)
f = open('input.txt', 'r')
n = int(f.read())
#1, 1, 2, 3, 5, 8, 13, 21
import copy
# n = 3
x = 0
y = 1
# m = copy.deepcopy(n)
fib_list = [1, 1]
m = n


def fibonachi(n, x, y):
    if n >= 1:
        # print(n, x, y)
        # print(fib_list)
        fib_list.append((fib_list[x]+fib_list[y]) % 10)
        x += 1
        y += 1
        n = n - 1
        fibonachi(n, x, y)
    else:
        # print('m=', m)
        return print(fib_list[m])


fibonachi(n, x, y)