from itertools import accumulate as acc


def dis(x, y):
    return (x + 1) * (y > 0)


def conv_pos(h_home):
    dist = []
    for position, string in enumerate(h_home):
        if string:
            dist.append(position + 1)
        else:
            dist.append(string)
    return dist


def nerest_zero(h_len, h_num):
    indices = [i + 1 for i, x in enumerate(h_num) if x == 0]
    result = []
    if h_num:
        for i in list(acc(h_num[(indices[0]-1)::-1], dis))[::-1]:
            if i:
                result.append(i)
        h_num = h_num[(indices[0] - 1)::]
    for f, b in zip(list(acc(h_num, dis)), list(acc(h_num[::-1], dis))[::-1]):
        result.append(min(f, b))
    return result


if __name__ == "__main__":
    street_lenth = input()
    home_number = [int(i) for i in input().split()]
    print(*nerest_zero(street_lenth, conv_pos(home_number)))
