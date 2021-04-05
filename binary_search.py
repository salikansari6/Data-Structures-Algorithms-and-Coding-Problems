def binary_search_recur(low, high, arr, value):
    mid = (low + high) // 2
    if low == high:
        return -1
    if value == arr[mid]:
        return mid
    if value > arr[mid]:
        return binary_search_recur(mid + 1, high, arr, value)
    else:
        return binary_search_recur(low, mid - 1, arr, value)


def binary_search(arr, value):
    low = 0
    high = len(arr) - 1
    mid = (low + high) // 2
    while arr[mid] != value and low <= high:
        if value < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
        mid = (low + high) // 2
    if arr[mid] == value:
        return mid
    return -1


array = [1, 4, 5, 7, 9]
print(binary_search_recur(0, len(array) - 1, array, 5))
print(binary_search(array, 9))
