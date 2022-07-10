def matrix():
    lin = int(input())
    col = int(input())
    matrix = []
    neighbors = []
    while len(matrix) != lin:
        line = input().split()
        if len(line) == col:
            matrix.append(line)
        else:
            print(f"Столбцов должно быть {col}")
    coo_lin = int(input())
    coo_col = int(input())
    nei_coords = [
        [int(coo_lin), int(coo_col) - 1],
        [int(coo_lin) + 1, int(coo_col)],
        [int(coo_lin), int(coo_col) + 1],
        [int(coo_lin) - 1, int(coo_col)]
        ]
    for coord in nei_coords:
        if 0 <= coord[0] < lin and 0 <= coord[1] < col:
            neighbors.append(int(matrix[coord[0]][coord[1]]))
    neighbors.sort()
    return neighbors


print(*matrix())
