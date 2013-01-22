def digitCount(n):
    s = 0
    while n > 0:
        mod = n % 10
        n /= 10
        s += 1
    return s

