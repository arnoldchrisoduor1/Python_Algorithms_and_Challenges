def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    #selet a pivot
    pivot = arr[-1]

    #partitioning
    left = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    #recusrion
    sorted_arr = quick_sort(left) + equal + quick_sort(right)

    return sorted_arr

if __name__ == '__main__':
    unsorted_list = [56, 78, 3, 5, 3, 5, 12, 45, 67, 45]
    print("This is the unsorted list: ", unsorted_list)
    sorted_list = quick_sort(unsorted_list)
    print("sorted_list: ", sorted_list)