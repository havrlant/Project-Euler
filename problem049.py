import math
from itertools import *

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

# Zbytecne pomale, nevedel jsem, ze tam musi byt ta podminka o rozdilu 3330
def candidates():
    for comb in combinations_with_replacement('0123456789', 4):
        res = {p for p in imap(lambda x: int("".join(x)), permutations(comb)) if isPrime(p) and p > 1000}
        res = sorted(res)
        if len(res) >= 3: 
            yield res

from time import time
s = time()

for cand in candidates():
    temp = set()
    for a,b in combinations(cand, 2):
        if abs(a-b) == 3330:
            temp.add(a)
            temp.add(b)
    if len(temp) == 3:
        temp = sorted(temp)
        print temp, "".join(imap(str, temp))

print time() - s