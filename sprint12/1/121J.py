from collections import Counter
n = input()
x = list(map(int, input().split()))
# list_x = input().split()
# print(x)
c = Counter(x)
# print(c.most_common())
if c.most_common()[0][1] == 2:
    print(c.most_common()[-1][0])
else:
    print(c.most_common()[0][0])
