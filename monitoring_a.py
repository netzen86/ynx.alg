def transpon(lin, col):
    matrix = []
    while len(matrix) != lin:
        line = input().split()
        if len(line) == col:
            matrix.append(line)
        else:
            print(f"Столбцов должно быть {col}")
    return zip(*matrix)


if __name__ == '__main__':
    lin = int(input())
    col = int(input())
    mtx = transpon(lin, col)
    for lin in mtx:
        print(*lin)
