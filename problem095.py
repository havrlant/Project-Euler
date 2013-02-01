import math
from time import time
from euler import primesBelow
from itertools import *


t = time()


def sumDivisors(n):
    s = 1
    sq = math.sqrt(n)
    for x in xrange(2, int(sq) + 1):
        if n % x == 0:
            s += x
            s += n / x
    if int(sq) == sq:
        s -= sq
    return int(s)

# primes = set(primesBelow(100000))
# sums = [set(), set()]

# for i in xrange(2, 100000):
#     if i in primes:
#         sums.append({1})
#         continue

#     if i % 2 == 0:
#         sums.append(sums[i / 2] | {i / 2, 2})
#         continue

#     divideBy = 2 if i % 2 == 0 else 3
#     for test in xrange(3, i, 2):
#         if i % test == 0:
#             div = i / test
#             s = {test, div} | sums[test] | sums[div]
#             sums.append(s)
#             break

# print sumDivisors(6)
# res = map(sum, sums[1:])
res = [sumDivisors(x) for x in xrange(1, 1000000)]

# print res[:40]
# print [sumDivisors(x) for x in xrange(1, 41)]
print sumDivisors(12)
print time() - t