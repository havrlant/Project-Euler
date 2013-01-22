from itertools import *

def fraction():
    last = ""
    for num in count():
        if last == "":
            last = str(num)
        while last != "":
            yield last[0]
            last = last[1:]

def isPower10(n):
    for i in xrange(7):
        if 10 ** i == n:
            return True
    return False

print reduce(lambda a,b:a*b, map(int, (v for i, v in enumerate(islice(fraction(), 1000005)) if isPower10(i))))