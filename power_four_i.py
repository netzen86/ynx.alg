# https://www.techiedelight.com/ru/check-given-number-power-of-4/
def power_four(number):
    # возвращает true, если `n` является степенью числа 2, и
    # остаток равен 1 при делении на 3
    if ((number & (number - 1)) == 0) and (number % 3 == 1):
        return True
    else:
        return False


if __name__ == '__main__':
    number = int(input())
    print(power_four(number))
