from euler import primes

def stPrime(n):
    for index, pr in enumerate(primes(), 1):
        if index == n:
            return pr

print stPrime(10001)