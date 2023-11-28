def twosum(num, target):
    for i in range(len(num) - 1):
        for j in range(i+1, len(num)):
            if num[i] + num[j] == target:
                return (i, j)
    return None