from itertools import *
import math
from collections import Counter


def cache(fun):
    dtb = {}
    def tempFun(n):
        temp = dtb.get(n, None)
        if temp is None:
            temp = fun(n)
            dtb[n] = temp
        return temp
    return tempFun

@cache
def isPrime(n):
    if n % 2 == 0:
        return False
    for i in xrange(3, int(math.sqrt(n)+1), 2):
        if n % i == 0: 
            return False
    return True

def oddComposite():
    for i in count(9, 2):
        if not isPrime(i):
            yield i

def decompose(n):
    for tosq in count(1):
        sq = 2 * (tosq * tosq)
        if sq >= n:
            return False
        if not isPrime(n - sq):
            continue
        return True


from time import time

s = time()
for x in oddComposite():
    if not decompose(x):
        print x
        break
print time() - s











# def prime_factorize(n):
#     factors = []
#     number = math.fabs(n)

#     while number > 1:
#         factor = get_next_prime_factor(number)
#         factors.append(factor)
#         number /= factor

#     if n < -1: # If we'd check for < 0, -1 would give us trouble
#         factors[0] = -factors[0]

#     return tuple(factors)

# def get_next_prime_factor(n):
#     if n % 2 == 0:
#         return 2

#     # Not 'good' [also] checking non-prime numbers I guess?
#     # But the alternative, creating a list of prime numbers,
#     # wouldn't it be more demanding? Process of creating it.
#     for x in range(3, int(math.ceil(math.sqrt(n)) + 1), 2):
#         if n % x == 0:
#             return x

#     return int(n)

# def factors(n):
#     counter = Counter(prime_factorize(n))
#     return [k**v for k,v in foo.iteritems()]