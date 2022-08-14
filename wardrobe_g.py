def item_color_sort(item_color):
    low = []
    mid = []
    high = []
    for item in item_color:
        if item == '0':
            low.append(item)
        elif item == '1':
            mid.append(item)
        else:
            high.append(item)
    print(*(low + mid + high))


if __name__ == '__main__':
    item_amount = input()
    item_color = input().split()
    item_color_sort(item_color)
