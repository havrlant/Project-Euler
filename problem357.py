from euler import isPrime, primes
from itertools import takewhile

candidates = set()
upto = int(100000001 / 2)

setOfPrimes = set(takewhile(lambda x: x <= upto, primes()))

# for d in xrange(1, upto):
    # pass
    # if isPrime(int(d+30/d)):
    #     candidates.add(d)

# for i in xrange(2, upto):
#     for d in xrange(i, upto, i):
#         if d in candidates:
#             if not isPrime(int(d+30/d)):
#                 candidates.remove(d)