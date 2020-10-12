n = int(input())
point_list = list(input().split())
space = ' '
count = 0
for i in point_list:
    if count == len(point_list)-1:
        space = ''
    count = count + 1
    if i == '0':
        continue
    print(i, end=space)
