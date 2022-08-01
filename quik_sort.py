
def partition(array, pivot):
    left = [item for item in array if item < pivot]
    center = [item for item in array if item == pivot]
    right = [item for item in array if item > pivot]
    return left, center, right


def quicksort(array):
    if len(array) < 2:  # базовый случай,
        return array  # массивы с 0 или 1 элементами фактически отсортированы
    else:  # рекурсивный случай
        pivot = array[(int(len(array) / 2))]
        left, center, right = partition(array, pivot)
        return quicksort(left) + center + quicksort(right)


if __name__ == '__main__':
    array = [23, 13, 56, 78, 45]
    print(quicksort(array))
