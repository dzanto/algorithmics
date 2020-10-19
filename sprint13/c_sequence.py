short_string = list(input())
long_string = list(input())
# print(short_string)
# print(long_string)
count = 0
yes = False
for i in long_string:
    if i == short_string[count]:
        print(i, count)
        if count == len(short_string)-1:
            print(True)
            yes = True
            break
        count += 1
        # if count == len(short_string)-1:
        #     break
print('end for')
print(count)
if count <= len(short_string)-1 and yes is not True:
    print(False)
