key_board = []
points = 0

k = (int(input()) * 2)

while len(key_board) != 16:
    key_board.extend([int(i) if i.isdigit() else 0 for i in list(input())])

for i in range(1, 10):
    if 0 < key_board.count(i) <= k:
        points += 1

print(points)
