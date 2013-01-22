from itertools import combinations_with_replacement
from math import factorial
from time import time

t = time()

factorials = [factorial(x) for x in xrange(10)]

# 175 -> 1^2+7^2+5^2
def digitPowers(n):
    return sum(x*x for x in n)

def combinationCount(k, n):
    return factorials[n] / (factorials[n-k]*factorials[k])

# 175 -> [5, 7, 1]
def getDigits(n):
    digits = []
    while n > 0:
        residue = n % 10
        n /= 10
        digits.append(residue)
    return digits

# [7,8,6,7,7,5] -> {8: 1, 5: 1, 6: 1, 7: 3}
def getCounter(n):
    d = {}
    for x in n:
        res = d.get(x, False)
        if not res:
            res = 0
        d[x] = res + 1
    return d

# Determine the end of the first 567 numbers
def getFirst567DigitNumbers():
    cachedDigitPowers = [False for x in xrange(1, 7*(9**2) + 2)]
    for i in xrange(1, 7*(9**2) + 1):
        orig = i
        while True:
            if i == 1: break
            if i == 89:
                cachedDigitPowers[orig] = True
                break
            i = digitPowers(getDigits(i))
    return cachedDigitPowers

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
    cachedDigitPowers = getFirst567DigitNumbers()
    for c in xrange(1, 8):
        for comb in combinations_with_replacement(range(1, 10), c): 
            if cachedDigitPowers[digitPowers(comb)]:
                yield comb

# Count all permutations: eg. if 1255 is in stucksIn89, then
# 1552, 5152, 51520, 15052, ... stucks in 89 too.
def getAllCombsCount():
    return (permutationsCount(getCounter(num).values()) for num in getCombinations())

print sum(getAllCombsCount()) == 8581146 # Yay! 
print time() - t