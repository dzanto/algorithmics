# n = list(map(int, input().split()))
# k = int(input())


# space = ' '
# for i in range(k):
#     tmp_max = max(set(n), key=n.count)
#     n = [x for x in n if x != tmp_max]
#     if i == k-1:
#         space = ''
#     print(tmp_max, end=space)

n = [1, 2, 3, 1, 2, 3, 3, 4]
k = 3
from collections import Counter
occurence_count = Counter(n)
space = ' '
for i in range(k):
    if i == k-1:
        space = ''
    print(occurence_count.most_common(k)[i][0], end=space)
