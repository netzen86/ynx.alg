import time


def find_pivot(arr, low, high):
    '''
    Python Program to search an element
    in a sorted and pivoted array
    Searches an element key in a pivoted
    sorted array arrp[] of size n
    Function to get pivot. For array
    3, 4, 5, 6, 1, 2 it returns 3
    (index of 6)
    '''
    # base cases
    if high < low:
        return -1
    if high == low:
        return low

    # low + (high - low)/2;
    mid = int((low + high)/2)

    if mid < high and arr[mid] > arr[mid + 1]:
        return mid
    if mid > low and arr[mid] < arr[mid - 1]:
        return (mid-1)
    if arr[low] >= arr[mid]:
        return find_pivot(arr, low, mid-1)
    return find_pivot(arr, mid + 1, high)


# Standard Binary Search function
def binary_search(arr, low, high, key):

    if high < low:
        return -1

    # low + (high - low)/2;
    mid = int((low + high)/2)

    if key == arr[mid]:
        return mid
    if key > arr[mid]:
        return binary_search(arr, (mid + 1), high,
                            key)
    return binary_search(arr, low, (mid - 1), key)


def broken_search(nums, target) -> int:
    n = len(nums)
    pivot = find_pivot(nums, 0, n-1)

    # If we didn't find a pivot,
    # then array is not rotated at all
    if pivot == -1:
        return binary_search(nums, 0, n-1, target)

    # If we found a pivot, then first
    # compare with pivot and then
    # search in two subarrays around pivot
    if nums[pivot] == target:
        return pivot
    if nums[0] <= target:
        return binary_search(nums, 0, pivot-1, target)
    return binary_search(nums, pivot + 1, n-1, target)


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]

    assert broken_search(arr, 5) == 6


if __name__ == '__main__':
    length = int(input())
    target = int(input())
    array = [int(i) for i in input().split()]
    print(broken_search(array, target))
