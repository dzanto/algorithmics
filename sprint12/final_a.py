# 36847993
CALC = {
    '+': (lambda a, b: b + a),
    '-': (lambda a, b: b - a),
    '*': (lambda a, b: b * a),
    '/': (lambda a, b: b // a),
}


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


def get_result(expression):
    list_nums = Stack()

    for i in expression:
        if i not in CALC:
            list_nums.push(i)
        else:
            x = CALC[i](list_nums.pop(), list_nums.pop())
            list_nums.push(x)

    return list_nums.pop()


if __name__ == "__main__":
    expression = list(input().split())
    print(get_result(expression))
