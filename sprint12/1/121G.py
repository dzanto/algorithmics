def anagram(first, second):
    first = list(first)
    second = list(second)
    first.sort()
    second.sort()
    if first == second:
        print('True')
    else:
        print('False')


first = input()
second = input()
anagram(first, second)
