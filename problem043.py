from itertools import permutations, ifilter, izip, imap
from time import time

t = time()

primes = [2, 3, 5, 7, 11, 13, 17]

def digitsToInt(digits):
    num, exp = 0, 9
    for d in digits:
        num += (10**exp) * d
        exp -= 1
    return num

def getDigits(n):
    digits = []
    while n > 0:
        residue = n % 10
        n /= 10
        digits.append(residue)
    return tuple(reversed(digits + ([0] * (3-len(digits)))))

def combine((a, b, c)):
    return a + b + c

def uniqueDigits(x):
    return len(set(x)) == len(x)

def getCandidates():
    return ifilter(uniqueDigits, imap(combine, findPairs()))

def addMissingDigit(tup, alldigits = {0,1,2,3,4,5,6,7,8,9}):
    missing = list(alldigits - set(tup))[0]
    return tuple([missing]) + tup

def getNumbers():
    return imap(digitsToInt, imap(addMissingDigit, getCandidates()))

def compatiblePairs(p1, p2):
    return p1[1] == p2[0] and p1[2] == p2[1]

divs = {pr:set(ifilter(uniqueDigits, imap(getDigits, xrange(pr, 1000, pr)))) for pr in primes}
iseven = lambda x: x in [0,2,4,6,8]

# d6 has to be 5
divs[7] = set(ifilter(lambda (a,b,c): b == 5, divs[7]))
divs[11] = set(ifilter(lambda (a,b,c): a == 5, divs[11]))

# d4 has to be even
divs[3] = set(ifilter(lambda (a,b,c): iseven(b), divs[3]))
divs[5] = set(ifilter(lambda (a,b,c): iseven(a), divs[5]))

def findPairs():
    for nas17 in divs[17]:
        for nas13 in divs[13]:
            if compatiblePairs(nas13, nas17):
                for nas11 in divs[11]:
                    if compatiblePairs(nas11, nas13):
                        for nas7 in divs[7]:
                            if compatiblePairs(nas7, nas11):
                                for nas5 in divs[5]:
                                    if compatiblePairs(nas5, nas7):
                                        for nas3 in divs[3]:
                                            if compatiblePairs(nas3, nas5):
                                                for nas2 in divs[2]:
                                                    if compatiblePairs(nas2, nas3):
                                                        yield nas2, nas7, nas17


print sum(getNumbers())
print time() - t