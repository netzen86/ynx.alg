def binary_search(money, price, left, right):
    if (right <= left and left != 0):
        return -1
    middle = (left + right) // 2
    if (money[middle] >= price and (money[middle - 1] < price or middle == 0)):
        return middle + 1
    elif price <= money[middle]:
        return binary_search(money, price, left, middle)
    else:
        return binary_search(money, price, middle + 1, right)


if __name__ == '__main__':
    day_quantity = int(input())
    money = [int(coin) for coin in input().split()]
    price = int(input())
    print(binary_search(money, price, left=0, right=len(money)), end=' ')
    print(binary_search(money, price * 2, left=0, right=len(money)))
