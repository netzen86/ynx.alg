def calc_x(mum):
    num = mum.split()
    # a, x, b, c.
    # y = ax2 + bx + c
    return (
        (int(num[0]) * (int(num[1]) ** 2)) +
        (int(num[2]) * int(num[1])) + int(num[3])
    )


numbers = input()
print(calc_x(numbers))
