from collections import Counter
x = input()
list_x = input().split()
c = Counter(list_x)
print(c.most_common(1)[0][0])
