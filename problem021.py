import math
from time import time

def divisors(n):
    divs = {1}
    for i in xrange(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divs |= {i, n / i}
    return divs

def sumdivs(n):
    return sum(divisors(n))

s = time()
amicable = set()
for i in xrange(1, 10000):
    divi = sumdivs(i)
    if sumdivs(divi) == i and i != divi:
        amicable.add(i)
        amicable.add(divi)

print sum(amicable)
print time() - s