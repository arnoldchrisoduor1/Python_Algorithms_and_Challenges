def solution(order, max_e):
    result = []
    ocurrences = {}

    for num in order:
        if num not in ocurrences:
            ocurrences[num] = 1
            result.append(num)
        elif ocurrences[num] < max_e:
            ocurrences[num] += 1
            result.append(num)

    return result