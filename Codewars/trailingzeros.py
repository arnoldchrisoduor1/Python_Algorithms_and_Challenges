#Finding the traiing zeros of the factorial of a number without calculating the factorial.

#We count the number of times the factorial includes factors of 5 - a trailing zero is created by pairs of 2s and 5s in the prime factorization of the factorial.

def zeros(n):
    count = 0
    i = 5
    while n // i >= 1:
        count += n // i
        i *= 5
    return count


