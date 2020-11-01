from operator import itemgetter
v = int(input())
n = int(input())
items = []
for i in range(n):
    items.append([int(i) for i in input().split()])
for i in range(len(items)):
    items[i].insert(0, i)
items.sort(key=itemgetter(1), reverse=True)
coast_dict = {}
num = 0
coast = 1
weight = 2
for i in items:
    if i[coast] not in coast_dict:
        coast_dict[i[coast]] = []
    coast_dict[i[coast]].append([i[num], i[weight]])
bag = []
for coast in coast_dict:
    coast_dict[coast].sort(key=itemgetter(1, 0))
    for item in coast_dict[coast]:
        if item[1] <= v:
            bag.append(item)
            v -= item[1]
bag.sort(key=itemgetter(0))
end = ' '
for i in bag:
    if i is bag[-1]:
        end = ''
    print(i[0], end=end)




# bagage = []
# bagage.append(sort_items[0])
# bag_cnt = 0

# for i in sort_items:
#     if i[weight] <= v:
#         if i[coast] == bagage[bag_cnt][coast] and i[weight] < bagage[bag_cnt][weight]:
#             bagage[bag_cnt] = i
#             continue
#         if i[coast] == bagage[bag_cnt][coast] and i[weight] == bagage[bag_cnt][weight] and i[num] < bagage[bag_cnt][num]:
#             bagage[bag_cnt] = i
#             continue
#         # if i[coast] < bagage[bag_cnt][coast]:
#         bagage.append(i)
#         bag_cnt += 1
#         v -= i[2]
#     elif v == 0:
#         break
# answer = []
# for i in range(len(items)):
#     if items[i] in bagage:
#         answer.append(i)
# print(' '.join(map(str, answer)))
