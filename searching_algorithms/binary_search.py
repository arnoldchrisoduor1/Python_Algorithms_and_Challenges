def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return mid
        if mid_value < target:
            low = mid + 1
        if mid_value > target:
            high = mid - 1

    return -1