from euler import *
from collections import Counter

def fact(n):
    counter = Counter(factors(n))
    return {k**v for k, v in counter.iteritems()}


i = 644
while True:
    fs = fact(i)
    tempfs = []
    if len(fs) == 4:
        ok = True
        for index, num in enumerate(xrange(i+1, i+4)):
            currfs = fact(num)
            if len(currfs) == 4:
                tempfs.append(currfs)
            else:
                ok = False
                break 
        if ok:
            allfs = [fs] + tempfs
            print i, allfs
            break
        else:
            i += index + 2
    else:
        i += 1