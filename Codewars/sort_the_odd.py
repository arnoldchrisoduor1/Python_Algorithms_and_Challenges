def sort_odd_numbers(arr):
    #identifying the odd numbers.
    odd_numbers = [(num, index) for index, num in enumerate(arr) if num % 2 !=0]

    #sort the odd numbers
    sorted_odd_numbers = sorted(odd_numbers, key = lambda x:x[0])

    #replacing the original odd numbers with the newly sorted numbers.
    for sorted_num, index in sorted_odd_numbers:
        arr[index] = sorted_num

    return arr