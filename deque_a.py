# ID посылки 69452723
class Deque:
    '''Класс реализующий структуру данных "дек"'''
    def __init__(self, n):
        self.__queue = [None] * n
        self.max = n
        self.head = -1
        self.tail = 0

    def queue(self):
        '''Выводит содержимое очереди'''
        return self.__queue

    def is_empty(self):
        '''Возвращает True если очередь пустая'''
        return self.head == -1

    def is_full(self):
        '''Возвращает True если очередь полностью заполнена'''
        return (self.head == 0
                and self.tail == self.max - 1
                or self.head == self.tail + 1)

    def push_front(self, item):
        '''Добавляет элемент в начало очереди'''
        if self.is_full():
            print('error')
            return 'error'
        if self.is_empty():
            self.head = 0
            self.tail = 0
        elif self.head == 0:
            # выставляем указатель головы на последний элемент очереди
            self.head = self.max - 1
        else:
            # выставляем указатель головы слева от текущей позиции
            self.head = self.head - 1
        self.__queue[self.head] = item

    def push_back(self, item):
        '''Добавляет элемент в конец очереди'''
        if self.is_full():
            print('error')
            return 'error'
        if self.is_empty():
            self.head = 0
            self.tail = 0
        elif self.tail == self.max - 1:
            # выставляем указатель хвоста на первый элемент очереди
            self.tail = 0
        else:
            # выставляем указатель хвоста справа от текущей позиции
            self.tail = self.tail + 1
        self.__queue[self.tail] = item

    def pop_front(self):
        '''Удаляет элемент с начала очереди'''
        if self.is_empty():
            return 'error'
        head = self.__queue[self.head]
        self.__queue[self.head] = None
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
        elif self.head == self.max - 1:
            # выставляем указатель головы на первый элемент очереди
            self.head = 0
        else:
            # выставляем указатель головы справа от текущей позиции
            self.head = self.head + 1
        return head

    def pop_back(self):
        '''Удаляет элемент с конца очереди'''
        if self.is_empty():
            return 'error'
        tail = self.__queue[self.tail]
        self.__queue[self.tail] = None
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
        elif self.tail == 0:
            # выставляем указатель хвоста на последний элемент очереди
            self.tail = self.max - 1
        else:
            # выставляем указатель хвоста слева от текущей позиции
            self.tail = self.tail - 1
        return tail


if __name__ == '__main__':
    num_cmds = int(input())
    max = int(input())
    dq = Deque(max)
    while num_cmds:
        cmd = input()
        if 'pop' in cmd or 'queue' in cmd:
            print(getattr(dq, cmd)())
        else:
            cmd = cmd.split()
            getattr(dq, cmd[0])(int(cmd[1]))
        num_cmds -= 1
