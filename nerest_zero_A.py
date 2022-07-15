# nerest_zero_a.py
# ID успешной посылки 69396321
from itertools import accumulate as acc


def dis(x, y):
    return (x + 1) * (y > 0)


def conv_pos(h_home):
    return [
        (int(pos) + 1)
        if val != "0"
        else int(val)
        for pos, val
        in enumerate(h_home)
        ]


def nerest_zero(h_num):
    indices = [i + 1 for i, x in enumerate(h_num) if x == 0]
    result = []
    for i in list(acc(h_num[(indices[0]-1)::-1], dis))[::-1]:
        if i:
            result.append(i)
    h_num = h_num[(indices[0] - 1)::]
    for f, b in zip(list(acc(h_num, dis)), list(acc(h_num[::-1], dis))[::-1]):
        result.append(min(f, b))
    return result


if __name__ == '__main__':
    street_length = input()
    home_number = input().split()
    print(*nerest_zero(conv_pos(home_number)))
