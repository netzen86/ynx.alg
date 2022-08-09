from typing import Union


class MyQueueSized:
    def __init__(self, max) -> None:
        self.max_size: int = max
        self.head: int = 0
        self.tail: int = 0
        self.q_size: int = 0
        self.__queue: list = [None] * max

    def push(self, item) -> Union[str, None]:
        if self.q_size == self.max_size:
            return 'error'
        self.__queue[self.tail] = item
        self.tail = (self.tail + 1) % self.max_size
        self.q_size += 1
        return None

    def pop(self) -> Union[int, None]:
        if not self.q_size:
            return None
        item = self.__queue[self.head]
        self.__queue[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.q_size -= 1
        return item

    def peek(self) -> int:
        item = self.__queue[self.head]
        return item

    def size(self) -> int:
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
