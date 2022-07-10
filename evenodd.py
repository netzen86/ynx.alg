def even_odd(num):
    num = num.split()
    if (int(num[0]) % 2) == (int(num[1]) % 2) == (int(num[2]) % 2):
        return "WIN"
    else:
        return "FAIL"


num = input()

print(even_odd(num))
