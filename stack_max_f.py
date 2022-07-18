class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


class StackMax(Stack):
    def __init__(self):
        super().__init__()

    def get_max(self):
        if self.items:
            max = sorted(self.items)
            print(max[-1])
        else:
            print(None)

    def pop(self):
        if not self.items:
            print('error')
        else:
            return self.items.pop()


if __name__ == '__main__':
    stack = StackMax()
    counter = 0
    num_cmds = int(input())
    while num_cmds:
        cmd = input()
        if "push" in cmd:
            cmd = cmd.split()
            getattr(stack, cmd[0])(int(cmd[1]))
        else:
            getattr(stack, cmd)()
        num_cmds -= 1
