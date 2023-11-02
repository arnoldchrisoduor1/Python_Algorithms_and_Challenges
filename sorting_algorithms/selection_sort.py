def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        #finding the minimum element in the unsorted list:
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        #swap the minimu elemnt with the firts element in the unsorted list:
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

if __name__ == '__main__':
    unsorted_list = [56, 78, 3, 5, 3, 5, 12, 45, 67, 45]
    print("This is the list of the unsorted list: ", unsorted_list)
    sorted_list = selection_sort(unsorted_list)
    print("This is the sorted list: ", sorted_list)