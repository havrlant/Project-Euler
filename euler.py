import math
from itertools import *
import operator

def cached(fun):
    dtb = {}
    def tempFun(n):
        temp = dtb.get(n, None)
        if temp is None:
            temp = fun(n)
            dtb[n] = temp
        return temp
    return tempFun

def isPrime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in xrange(3, int(math.sqrt(n)+1), 2):
        if n % i == 0: 
            return False;
    return True;

def isEven(n):
    return n % 2 == 0

def isOdd(n):
    return n % 2 == 1

def fib():
    a, b = 0, 1
    while 1:
        yield a
        a, b = b, a + b

def divisors(n):
    sq = math.sqrt(n)
    isq = int(sq)
    notSquare = isq != sq
    for i in xrange(2, isq + notSquare):
        if n % i == 0:
            yield i
            yield int(n / i)
    if not notSquare:
        yield isq

def factors(n):
    factors = []
    number = math.fabs(n)

    while number > 1:
        factor = _get_next_prime_factor(number)
        factors.append(factor)
        number /= factor

    if n < -1: 
        factors[0] = -factors[0]

    return tuple(factors)

def primes():
    yield 2
    x = 3
    while True:
        if isPrime(x):
            yield x
        x += 2

def primesBelow(n):
    sieve = [True] * (n + 1)
    sieve[0], sieve[1] = False, False
    for i in xrange(2, int(math.sqrt(n)) + 1):
        if sieve[i]:
            for j in xrange(i**2, n+1, i):
                sieve[j] = False
    return (i for i, x in enumerate(sieve) if x)

def prod(n):
    return reduce(operator.mul, n)

def digitsToNum(digits):
    num = digits[0]
    for digit in digits[1:]:
        num *= 10
        num += digit
    return num

@cached
def _get_next_prime_factor(n):
    if n % 2 == 0:
        return 2

    for x in range(3, int(math.ceil(math.sqrt(n)) + 1), 2):
        if n % x == 0:
            return x

    return int(n)