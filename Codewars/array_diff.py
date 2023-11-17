def solution(arr1, arr2):
    unique = []
    for value in arr1:
        if value not in arr2:
            unique.append(value)

    for elements in arr2:
        if elements not in arr1:
            if elements not in unique:
                unique.append(elements)
    return unique

def solution2(a, b):
    return[item for item in a if item not in b]