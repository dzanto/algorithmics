from collections import Counter
a = list(input())
a.sort()
# print(a)
c = Counter(a)
# print(c.most_common())
for i in c.most_common():
    for n in range(i[1]):
        print(i[0], end='')

