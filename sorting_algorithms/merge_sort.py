def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    #dividing the list into half:
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    #recursively sorting both halves:
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    #conquer and merge:
    sorted_arr = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left_half) and right_idx < len(right_half):
        if left_half[left_idx] < right_half[right_idx]:
            sorted_arr.append(left_half[left_idx])
            left_idx += 1
        else:
            sorted_arr.append(right_half[right_idx])
            right_idx += 1

    #appending any remaining elements from the sublists:
    sorted_arr.extend(left_half[left_idx:])
    sorted_arr.extend(right_half[right_idx:])

    return sorted_arr

if __name__ == '__main__':
    unsorted_list = [56, 78, 3, 5, 3, 5, 12, 45, 67, 45]
    print("The usorted list:", unsorted_list)
    sorted_list = merge_sort(unsorted_list)
    print("Sorted list:", sorted_list)