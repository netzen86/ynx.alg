class MyQueueSized:
    def __init__(self, max) -> None:
        self.max_size: int = max
        self.q_size: int = 0
        self.__queue: list = [None] * max

    def pointer(self) -> int:
        if self.q_size == self.max_size:
            return self.q_size - 1
        return self.q_size

    def push(self, item) -> str:
        if self.max_size == self.q_size:
            return 'error'
        self.__queue[self.pointer()] = item
        self.q_size += 1
        return None

    def pop(self) -> int:
        if not self.q_size:
            return None
        item = self.peek()
        self.__queue[self.pointer()] = None
        self.q_size -= 1
        return item

    def peek(self):
        print(self.__queue)
        if not self.q_size:
            return None
        return self.__queue[self.pointer()]

    def size(self):
        return self.q_size


if __name__ == '__main__':
    num_cmds = int(input())
    max = int(input())
    sq = MyQueueSized(max)
    while num_cmds:
        cmd = input()
        if 'push' in cmd:
            cmd = cmd.split()
            msg = getattr(sq, cmd[0])(int(cmd[1]))
            if msg:
                print(msg)
        else:
            print(getattr(sq, cmd)())
        num_cmds -= 1
