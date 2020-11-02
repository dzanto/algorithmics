import string
lowercase = list(string.ascii_lowercase)
dict_low = {lowercase[i]: i for i in range(len(lowercase))}
for i in range(1,5):
    print(i)