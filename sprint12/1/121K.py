x = int(input())
x = bin(x)[2::]
list_x = list(str(x))
# print(list_x)
count = 0
for i in list_x:
    if i == '1':
        count += 1
print(count)

