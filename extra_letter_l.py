def extra_letter(native_str, blended_str):
    blended_str = sorted(blended_str)
    native_str = sorted(native_str)
    for iter in range(len(blended_str)):
        if blended_str[iter] not in native_str:
            return blended_str[iter]
        if blended_str[iter] != native_str[iter]:
            return blended_str[iter]


if __name__ == '__main__':
    native_str = input()
    blended_str = input()
    print(extra_letter(native_str, blended_str))
