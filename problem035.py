from euler import primesBelow
from time import time

s = time()
digits = {str(x) for x in {1,3,5,7,9}}
primes = {x for x in primesBelow(1000000) if set(str(x)) <= digits}
powers = [10**x for x in xrange(15)]

def circulars(n):
    yield n
    numlen = len(str(n)) - 1
    for i in xrange(numlen):
        lastDigit = n % 10
        n /= 10
        n += powers[numlen] * lastDigit
        yield n

def isCircular(n):
    return all(x in primes for x in circulars(n))


print len({x for x in primes if isCircular(x)})
print time() - s