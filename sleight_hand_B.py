# sleight_hand_b.py
# ID успешной посылки 69396370

def input_data():
    key_board = []
    while len(key_board) != 16:
        key_board.extend([int(i) if i.isdigit() else 0 for i in list(input())])
    return key_board


def speed_typing(keys, key_board):
    points = 0
    for i in range(1, 10):
        if 0 < key_board.count(i) <= keys:
            points += 1
    return points


if __name__ == '__main__':
    keys = (int(input()) * 2)
    print(speed_typing(keys, input_data()))
