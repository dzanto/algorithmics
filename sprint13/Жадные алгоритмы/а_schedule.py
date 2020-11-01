from operator import itemgetter

k = int(input())
schedule = []
for i in range(k):
    schedule.append(list(map(float, input().split())))
# print(schedule)
schedule = sorted(schedule, key=itemgetter(1, 0))
# print(schedule)
new_schedule = []
start = 0
end = 0

def integer(i):
    if i % 1 == 0:
        # print(i)
        return int(i)
    else:
        return i


for i in schedule:
    if i[0] >= end:
        new_schedule.append(i)
        start = i[0]
        end = i[1]
print(len(new_schedule))

int_schedule = []
for i in new_schedule:
    int_schedule.append(list(map(integer, i)))

for i in int_schedule:
    print(' '.join(map(str, i)))
