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
        else:
            print('error')

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


QUEUE_METHODS = {
    'pop':  (lambda queue: print(queue.get())),
    'peek': (lambda queue: print(queue.get_head())),
    'size': (lambda queue: print(queue.size)),
}


def solution(commands, queue_limit):
    queue = MyQueue(queue_limit)
    for command in commands:
        # print(command, queue.queue)
        if command[0] == 'push':
            queue.put(command[1])
        else:
            QUEUE_METHODS[command[0]](queue)



if __name__ == "__main__":
    number_of_command = int(input())
    queue_limit = int(input())
    commands = []
    for i in range(number_of_command):
        commands.append(list(input().split()))
    solution(commands, queue_limit)
