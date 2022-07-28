def bubble(ar_len, array):
    if ar_len == 1:
        return [array, ]
    end = 1
    result = []
    for ext_iter in range(ar_len - 1):
        f = 0
        for int_iter in range(ar_len - end):
            pointer1 = array[int_iter]
            pointer2 = array[int_iter + 1]
            if pointer1 > pointer2:
                array[int_iter], array[int_iter + 1] = pointer2, pointer1
                f = 1
        if f == 0:
            if len(result) > 1:
                return result
            return [array, ]
        end += 1
        result.append(array.copy())
    return result


if __name__ == '__main__':
    length = int(input())
    array = [int(i) for i in input().split()]
    [print(*item) for item in bubble(length, array)]
