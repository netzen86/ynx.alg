
def find_pivot(arr, low, high):
    '''Функция для поиска точки сдвига'''
    if high < low:
        return -1
    if high == low:
        return low
    mid = int((low + high)/2)
    if mid < high and arr[mid] > arr[mid + 1]:
        return mid
    if mid > low and arr[mid] < arr[mid - 1]:
        return (mid-1)
    if arr[low] >= arr[mid]:
        return find_pivot(arr, low, mid-1)
    return find_pivot(arr, mid + 1, high)


def binary_search(arr, low, high, key):
    '''Функция бинарного поиска'''
    if high < low:
        return -1
    mid = int((low + high)/2)
    if key == arr[mid]:
        return mid
    if key > arr[mid]:
        return binary_search(arr, (mid + 1), high, key)
    return binary_search(arr, low, (mid - 1), key)


def broken_search(nums, target) -> int:
    '''Функция поиска элемента в сдвинутом массиве'''
    n = len(nums)
    pivot = find_pivot(nums, 0, n-1)
    if pivot == -1:
        return binary_search(nums, 0, n-1, target)
    if nums[pivot] == target:
        return pivot
    if nums[0] <= target:
        return binary_search(nums, 0, pivot-1, target)
    return binary_search(nums, pivot + 1, n-1, target)


if __name__ == '__main__':
    length = int(input())
    target = int(input())
    array = [int(i) for i in input().split()]
    print(broken_search(array, target))
