def greedy_child(factor, sizes):
    happy_child = 0
    factor = sorted(list(map(int, factor)), reverse=True)
    sizes = sorted(list(map(int, sizes)))
    for i in range(len(factor)):
        if sizes and factor[i] <= sizes[-1]:
            sizes.pop()
            happy_child += 1
    return happy_child


if __name__ == '__main__':
    child_amount = input()
    factor = input().split()
    cookies_amount = input()
    sizes = input().split()
    print(greedy_child(factor, sizes))
