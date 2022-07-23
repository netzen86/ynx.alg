# ID посылки 69452741
class Stack:
    '''Класс реализующий структуру данных "стек"'''
    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        return self.__items.pop()


# словарь с помошью которого определяем арифметическое действие
ops = {
  '+': (lambda a, b: a + b),
  '-': (lambda a, b: a - b),
  '*': (lambda a, b: a * b),
  '/': (lambda a, b: int(a / b))
}


def calc(expr):
    '''Функция для вычисления выражений в обратной польской нотации'''
    nums = expr.split()
    stack = Stack()
    for num in nums:
        if num in ops:
            arg2 = stack.pop()
            arg1 = stack.pop()
            if arg1 < 0 and num == '/':
                result = arg1 // arg2
            else:
                result = ops[num](arg1, arg2)
            stack.push(result)
        else:
            stack.push(int(num))

    return stack.pop()


if __name__ == '__main__':
    expr = input()
    print(calc(expr))
