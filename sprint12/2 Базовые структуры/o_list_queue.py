class ListQueue:
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
            return 'error'
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x

    def get_head(self):
        return self.queue[self.head]



def list_queue(commands, number_of_command):
    queue = ListQueue(number_of_command)
    for command in commands:
        if command[0] == 'put':
            queue.put(command[1])
        elif command[0] == 'get':
            print(queue.get())
        else:
            print(queue.size)


if __name__ == '__main__':
    number_of_command = int(input())
    commands = []
    for i in range(number_of_command):
        commands.append(input().split())
    list_queue(commands, number_of_command)

