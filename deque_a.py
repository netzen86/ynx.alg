# ID посылки 69443645
class Deque:
    def __init__(self, n):
        self.queue = [None] * n
        self.max = n
        self.head = -1
        self.tail = 0

    def is_empty(self):
        return self.head == -1

    def is_full(self):
        return (self.head == 0
                and self.tail == self.max - 1
                or self.head == self.tail + 1)

    def push_front(self, item):
        if self.is_full():
            print('error')
            return 'error'
        if self.is_empty():
            self.head = 0
            self.tail = 0
        elif self.head == 0:
            self.head = self.max - 1
        else:
            self.head = self.head - 1
        self.queue[self.head] = item

    def push_back(self, item):
        if self.is_full():
            print('error')
            return 'error'
        if self.is_empty():
            self.head = 0
            self.tail = 0
        elif self.tail == self.max - 1:
            self.tail = 0
        else:
            self.tail = self.tail + 1
        self.queue[self.tail] = item

    def pop_front(self):
        if self.is_empty():
            return 'error'
        head = self.queue[self.head]
        self.queue[self.head] = None
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
        elif self.head == self.max - 1:
            self.head = 0
        else:
            self.head = self.head + 1
        return head

    def pop_back(self):
        if self.is_empty():
            return 'error'
        tail = self.queue[self.tail]
        self.queue[self.tail] = None
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
        elif self.tail == 0:
            self.tail = self.max - 1
        else:
            self.tail = self.tail - 1
        return tail


if __name__ == '__main__':
    num_cmds = int(input())
    max = int(input())
    dq = Deque(max)
    while num_cmds:
        cmd = input()
        if 'pop' in cmd:
            print(getattr(dq, cmd)())
        else:
            cmd = cmd.split()
            getattr(dq, cmd[0])(int(cmd[1]))
        num_cmds -= 1
