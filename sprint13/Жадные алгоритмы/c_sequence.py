short_string = list(input())
long_string = list(input())

count = 0
new_string = []
pop_string = short_string.copy()
for i in long_string:
    if pop_string == []:
        print(True)
        break
    if i == pop_string[0]:
        new_string.append(i)
        pop_string.pop(0)
        if short_string == new_string:
            print(True)
            break
if short_string != new_string:
    print(False)
