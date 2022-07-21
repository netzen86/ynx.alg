class MyQueueSized:
    def __init__(self) -> None:
        self.max_size = 0
        self.size = 0
        self.__queue = []

    def push(self, item):
        if self.max_size <= self.size:
            return 'error'
        self

    def pop(self):
        pass

    def peek(self):
        pass

    def size(self):
        pass
