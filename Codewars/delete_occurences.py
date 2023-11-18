def fun_occurrences(arr, max_e):
    result = []
    occurrences = {}
    for num in arr:
        if num not in occurrences:
            occurrences[num] = 1
            result.append(num)
        elif occurrences[num] < max_e:
              occurrences[num] += 1
              result.append(num)
    return result
