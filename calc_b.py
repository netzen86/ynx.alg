# ID посылки 69432422
ops = {
  '+': (lambda a, b: a + b),
  '-': (lambda a, b: a - b),
  '*': (lambda a, b: a * b),
  '/': (lambda a, b: int(a / b))
}


def calc(expr):
    nums = expr.split()
    stack = []
    for num in nums:
        if num in ops:
            arg2 = stack.pop()
            arg1 = stack.pop()
            if arg1 < 0 and num == '/':
                result = arg1 // arg2
            else:
                result = ops[num](arg1, arg2)
            stack.append(result)
        else:
            stack.append(int(num))

    return stack.pop()


if __name__ == '__main__':
    expr = input()
    print(calc(expr))
