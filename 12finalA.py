# 36598027
calc = {
    '+': (lambda a, b: b + a),
    '-': (lambda a, b: b - a),
    '*': (lambda a, b: b * a),
    '/': (lambda a, b: b // a),
}

expression = list(input().split())


class Stack:
    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(int(item))

    def pop(self):
        try:
            return self.__items.pop()
        except IndexError:
            raise IndexError('pop from empty stack')


if __name__ == "__main__":
    list_nums = Stack()

    for i in expression:
        if i not in calc:
            list_nums.push(i)
        else:
            x = calc[i](list_nums.pop(), list_nums.pop())
            list_nums.push(x)

    print(list_nums.pop())
