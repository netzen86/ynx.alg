def list_form(lst_frm, number):
    return list(str(lst_frm + number))


if __name__ == '__main__':
    lenth = int(input())
    lst_frm = int(''.join([symbol for symbol in input().split()]))
    number = int(input())
    print(*list_form(lst_frm, number))
