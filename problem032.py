from itertools import combinations, permutations
from euler import digitsToNum

def getLeftRight(productSize, leftSize, perm, digits = set([1,2,3,4,5,6,7,8,9])):
    product = digitsToNum(perm)
    residue = digits - set(perm)
    for left in permutations(residue, leftSize):
        leftNum = digitsToNum(left)
        for right in permutations(residue - set(left), 9 - productSize - leftSize): 
            rightNum = digitsToNum(right)
            if leftNum * rightNum == product:
                return product

def getMultis(productSize):
    for comb in combinations(range(1, 10), productSize):
        for perm in permutations(comb):
            for leftSize in xrange(1, int(productSize / 2) + 1):
                temp = getLeftRight(productSize, leftSize, perm)
                if temp: yield temp

print sum(getMultis(4))