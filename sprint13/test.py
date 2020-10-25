import string
lowercase = list(string.ascii_lowercase)
dict_low = {lowercase[i]: i for i in range(len(lowercase))}
print(dict_low)
