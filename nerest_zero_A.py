list = [2, 3, 4, 0, 5, 6, 0, 5, 67, 0]

indices = [i for i, x in enumerate(list) if x == 0]

print(indices)
