class Node:
    def __init__(self, item) -> None:
        self.item = item
        self.next = None


class ListQueue:
    def __init__(self) -> None:
        self.top = None
        self.tail = None
        self.lq_size = 0

    def get(self):
        result = 0
        if not self.top:
            return 'error'
        else:
            result = self.top.item
            self.top = self.top.next
            self.lq_size -= 1
            return result

    def put(self, item):
        new_node = Node(item)
        if self.top is None:
            self.top = new_node
            self.tail = self.top
        elif self.top == self.tail:
            self.top.next = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.lq_size += 1

    def size(self):
        return self.lq_size


if __name__ == '__main__':
    lq = ListQueue()
    num_cmds = int(input())
    while num_cmds:
        cmd = input()
        if "put" in cmd:
            cmd = cmd.split()
            getattr(lq, cmd[0])(int(cmd[1]))
        elif "size" in cmd:
            print(lq.size())
        elif "get" in cmd:
            print(lq.get())
        num_cmds -= 1
