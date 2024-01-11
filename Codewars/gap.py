def gap(g, m, n):
    def is_prime(num):
        if num < 2:
            return False
        
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    prev_prime = None

    for num in range(m, n + 1):
        if is_prime(num):
            if prev_prime is not None and num - prev_prime == g:
                return [prev_prime, num]
            prev_prime = num

    return None