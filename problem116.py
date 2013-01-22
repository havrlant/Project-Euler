from itertools import *

def isValid(grid):
    for line in grid:
        if sum(line) != 12:
            return False

    for col in zip(*grid):
        if sum(col) != 12:
            return False

    if (grid[0][0]+grid[1][1]+grid[2][2]+grid[3][3]) != 12:
        return False
    if (grid[0][3]+grid[1][2]+grid[2][1]+grid[3][0]) != 12:
        return False

    return True

def sum12():
    for comb in combinations_with_replacement('0123456789', 4):
        if sum(int(x) for x in comb) == 12:
            yield comb

def perm12():
    for comb in sum12():
        for perm in permutations(comb):
            yield perm

def isValidGrid(grid):
    if (grid[0][0]+grid[1][1]+grid[2][2]+grid[3][3]) != 12:
        return False
    if (grid[0][3]+grid[1][2]+grid[2][1]+grid[3][0]) != 12:
        return False
    # if set(imap(sum, izip(*grid))) != {12}:
    #     return False
    for col in izip(*grid):
        if sum(col) != 12:
            return False
    return True

def canBeCompleted(first, second):
    # if any(x > 12 for x in map(sum, zip(first, second))): return False
    # for col in izip(first, second):
    #     if sum(col) > 12:
    #         return False
    if first[1] + second[2] > 12: return False
    if second[3] + second[2] > 12: return False
    return True

def grids():
    combs = {tuple(map(int, x)) for x in perm12()}
    # print len(combs)
    for i, first in enumerate(combs):
        print i
        for second in combs:
            if canBeCompleted(first, second):
                for third in combs:
                    for last in combs:
                        grid = [first, second, third, last]
                        if isValidGrid(grid):
                            yield grid
                # grid = [first, second, third]
                # last = []
                # last.append(12 - (first[0] + second[0] + third[0]))
                # if last[0] < 0 or last[0] > 9: continue
                # last.append(12 - (first[1] + second[1] + third[1]))
                # if last[1] < 0 or last[1] > 9: continue
                # last.append(12 - (first[2] + second[2] + third[2]))
                # if last[2] < 0 or last[2] > 9: continue
                # last.append(12 - (first[3] + second[3] + third[3]))
                # if last[3] < 0 or last[3] > 9: continue
                # grid.append(last)
                # if isValidGrid(grid):
                #     yield tuple(map(tuple, grid))

def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))




# print [x for x in grids() if not isValid(x)]
# print take(5, grids())[2]

from time import time
s = time()
print "Vysledek: %s" % sum(1 for x in grids())
print time() - s


# Vysledek: 393757
# Vysledek: 202543
# Vysledek: 199081
# Vysledek: 209127