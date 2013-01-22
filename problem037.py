from itertools import ifilter
from euler import *

divs = map(lambda x: 10**x, xrange(1, 20))
def isRightTruncatable(n):
    for d in divs:
        res = n % d
        if res == n:
            return True
        elif not isPrime(res):
            return False

def leftTruncatable():
    add = [1, 3, 5, 7, 9]
    trunc = [23, 29, 31, 37, 53, 59, 71, 73, 79]    # all left trunc below 100

    for tr in trunc:
        temp = tr * 10
        for a in add:
            candidate = temp + a
            if isPrime(candidate):
                trunc.append(candidate)
        yield tr

print sum(ifilter(isRightTruncatable, leftTruncatable()))





# def isLeftTruncatable(n):
#     digits = map(int, str(n)[:-1])
#     i = 0
#     for digit in digits:
#         i *= 10
#         i += digit
#         if not isPrime(i):
#             return False
#     return True

# def isTruncatable(n):
#     return isRightTruncatable(n) and isLeftTruncatable(n)

# print sum(islice(ifilter(isTruncatable, dropwhile(lambda x: x < 10, primes())), 11))
# time = 0.00722789764404