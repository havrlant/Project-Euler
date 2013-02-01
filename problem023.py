divsums = [0 for x in xrange(28124)]

for i in xrange(1, 28124 / 2):
    for j in xrange(i*2, 28124, i):
        divsums[j] += i

def nonsums(divsums):
    abundants = set()
    for i, s in enumerate(divsums):
        if s > i:
            abundants.add(i)
        for a in abundants:
            if i - a in abundants:
                break
        else:
            yield i

print sum(nonsums(divsums))