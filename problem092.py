from itertools import combinations_with_replacement
from math import factorial
from time import time

t = time()

factorials = [factorial(x) for x in xrange(10)]

def digitPowers(n):
    return sum(x*x for x in n)

def combinationCount(k, n):
    return factorials[n] / (factorials[n-k]*factorials[k])

cachedDigitPowers = [False for x in xrange(1, 7*(9**2) + 2)]

# Determine the end of the first 567 numbers
for i in xrange(1, 7*(9**2) + 1):
    orig = i
    while True:
        if i == 1: break
        if i == 89:
            cachedDigitPowers[orig] = True
            break
        i = digitPowers(map(int, str(i)))

# Count all possible permutations of some tuple
# eg. [aaabbd] has 420 permutations: aaabbd, aaabdb, aaadbb, baabda, ...
# We compute it as: C(3,6)*C(2,3)*C(1,1), 
# where C(k,n) is number of combinations: C(k,n) = n!/((n-k)!*k!)
def permutationsCount(counter):
    holes, temp = 7, 1
    for v in counter:
        temp *= combinationCount(v, holes)
        holes -= v
    return temp

# Computes all _combinations_ of 123456789 of length 1..7,
# which stucks in 89
def getCombinations():
    toint = lambda x: reduce(lambda rst, d: rst * 10 + d, comb) # converts (1,2,3) to 123
    for c in xrange(1, 8):
        for comb in combinations_with_replacement(range(1, 10), c): 
            if cachedDigitPowers[digitPowers(comb)]:
                yield comb

def getCounter(n):
    d = {}
    for x in n:
        res = d.get(x, False)
        if not res:
            res = 0
        d[x] = res + 1
    return d

# Count all permutations: eg. if 1255 is in stucksIn89, then
# 1552, 5152, 51520, 15052, ... stucks in 89 too.
def getAllCombsCount():
    return (permutationsCount(getCounter(num).values()) for num in getCombinations())

print sum(getAllCombsCount()) # Yay! 
print time() - t