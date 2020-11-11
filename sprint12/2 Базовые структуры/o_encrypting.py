def encrypt(string, template):

    template.sort()
    count = 0
    for i in range(len(string) - len(template) + 1):
        sorted_slice = sorted(string[i:(i+len(template))])
        if sorted_slice == template:
            count += 1
    return count


if __name__ == '__main__':
    string = list(input())
    template = list(input())
    print(encrypt(string, template))
