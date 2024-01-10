def remov_nb(n):
    #calculate the sum of the numbers from 1 to n:
    total_sum = n * (n + 1) // 2

    result = []

    #iterate through all possible pairs (a, b)
    for a in range(1, n + 1):
        b = (total_sum - a) / (a + 1)
        #check if b is an integer within the valid range
        if b.is_integer() and 1 <= b <= n:
            result.append((a, int(b)))

    return result