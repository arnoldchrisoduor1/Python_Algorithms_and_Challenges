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

def solution2(order, max_e):
    ans = []
    for o in order:
        if ans.count(o) < max_e: ans.append(o)
    return ans