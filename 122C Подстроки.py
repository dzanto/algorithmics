string = list(input())
# print(string)
biggest_str = []
count = 0
for i in string:
    if i not in biggest_str:
        biggest_str.append(i)
        if count < len(biggest_str):
            count = len(biggest_str)
    else:
        # print(biggest_str, len(biggest_str), i)
        while i != biggest_str[0]:
            biggest_str.pop(0)
        biggest_str.pop(0)
        biggest_str.append(i)


# print(biggest_str, len(biggest_str))
print(count)
# pwwkew
# ojodx