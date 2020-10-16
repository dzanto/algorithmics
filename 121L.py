from collections import Counter
a = list(input())
b = list(input())
# print(a)
# print(b)
ac = Counter(a)
bc = Counter(b)
ab = list(set(ac.most_common()) ^ set(bc.most_common()))
print(ab[0][0])

