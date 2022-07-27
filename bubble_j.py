import time


def bubble(ar_len, array, stopper=0):
    f = 0
    if stopper == (ar_len - 1):
        return array
    for iter in range(ar_len - 1):
        pointer1 = array[iter]
        pointer2 = array[iter + 1]
        if pointer1 > pointer2:
            array[iter], array[iter + 1] = pointer2, pointer1
        else:
            f = 1
    if not f:
        return array
    stopper += 1
    print(array)
    return bubble(ar_len, array, stopper)


start = time.time()
print(bubble(5, [4, 3, 9, 2, 12]))
print(time.time() - start)
