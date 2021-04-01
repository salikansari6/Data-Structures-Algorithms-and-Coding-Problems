def count_unique_values(arr):
    i = 0
    j = i + 1
    while j != len(arr):
        if arr[i] == arr[j]:
            j += 1
        else:
            i += 1
            arr[i] = arr[j]
            j += 1
    return arr[:i + 1]


print(count_unique_values([1, 1, 1, 2, 3, 3, 4, 4, 5, 6, 7, 7, 7, 8, 8, 9]))
