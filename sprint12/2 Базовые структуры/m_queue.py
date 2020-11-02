class MyQueue:
    def __init__(self, n):
        self.queue = [None for _ in range(n)]
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def put(self, x):
        if self.size != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1

    def get(self):
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x

    def get_head(self):
        return self.queue[self.head]


def solution(commands, number_of_command):
    queue = MyQueue(number_of_command)
    for command in commands:
        if command[0] == 'push':
            queue.put(command[1])
        elif command[0] == 'pop':
            print(queue.get())
        elif command[0] == 'peek':
            print(queue.get_head())
        else:
            print(queue.size)
        # print(queue.queue)


if __name__ == "__main__":
    number_of_command = int(input())
    commands = []
    for i in range(number_of_command):
        commands.append(list(input().split()))
    solution(commands, number_of_command)
    # print(commands)
