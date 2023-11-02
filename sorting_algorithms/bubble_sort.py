def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if not swapped:
            break

if __name__ == '__main__':
    arr = [56, 78, 3, 5, 3, 5, 12, 45, 67, 45]
    print("Original array: ",arr)

    bubble_sort(arr)
    print("Sorted array:", arr)