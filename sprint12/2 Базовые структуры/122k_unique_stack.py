class Stack:
    def __init__(self):
        self.items = []
        self.stack_set = set()

    def push(self, item):
        if item not in self.stack_set:
            self.items.append(item)
            self.stack_set.add(item)

    def pop(self):
        if len(self.items) == 0:
            return print('error')
        self.stack_set.remove(self.items.pop())

    def peek(self):
        if len(self.items) == 0:
            return print('error')
        return print(self.items[len(self.items) - 1])

    def size(self):
        return print(len(self.items))


COMM = {
    # 'push': (lambda stack, a: stack.push(int(a))),
    'pop': (lambda stack: stack.pop()),
    'peek': (lambda stack: stack.peek()),
    'size': (lambda stack: stack.size()),
}


def solution(commands):
    stack = Stack()
    for command in commands:
        if command[0] == 'push':
            stack.push(int(command[1]))
        # elif command[0] == 'pop':
        #     stack.pop()
        # elif command[0] == 'peek':
        #     stack.peek()
        # else:
        #     stack.size()
        else:
            COMM[command[0]](stack)


if __name__ == "__main__":
    number_of_command = int(input())
    commands = []
    for i in range(number_of_command):
        commands.append(list(input().split()))
    solution(commands)
