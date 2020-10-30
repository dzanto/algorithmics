class StackMax:
    def __init__(self):
        self.items = []
        self.items.append(None)

    def push(self, item):
        if self.items[len(self.items) - 1] is None:
            self.items.append(item)
        elif item >= self.items[len(self.items) - 1]:
            self.items.append(item)

    def pop(self, item):
        if item == self.items[len(self.items) - 1]:
            return self.items.pop()

    def get_max(self):
        return self.items[len(self.items) - 1]


class Stack:
    def __init__(self):
        self.items = []
        self.stack_max = StackMax()

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
        self.stack_max.push(item)

    def pop(self):
        if len(self.items) == 0:
            return print('error')
        self.stack_max.pop(self.items[len(self.items) - 1])
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def solution(commands):
    stack = Stack()
    for command in commands:
        if command[0] == 'get_max':
            print(stack.stack_max.get_max())
        elif command[0] == 'pop':
            stack.pop()
        else:
            stack.push(int(command[1]))


if __name__ == "__main__":
    number_of_command = int(input())
    commands = []
    for i in range(number_of_command):
        commands.append(list(input().split()))
    solution(commands)
