def gen_bin_bracket(control, n1, n2, prefix):
    if n1 == 0 and n2 == 0:
        print(prefix)
    else:
        if n1 > 0:
            gen_bin_bracket(control + 1, n1 - 1, n2, prefix + '(')
        if (control > 0 and n2 > 0):
            gen_bin_bracket(control - 1, n1, n2 - 1, prefix + ')')


if __name__ == '__main__':
    n = int(input())
    control = 0
    n1 = n
    n2 = n
    gen_bin_bracket(control, n1, n2, '')
