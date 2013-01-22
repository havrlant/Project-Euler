#!/opt/local/bin/python
from euler import *
from itertools import *

def candidates(count = 10):
    mc = count - 1
    for perm in permutations('123456789'[:count]):
        num = int("".join(perm))
        if isPrime(num):
            yield num


from time import time
s = time()

# ostatni jsou vzdy necim delitelne
for i in [7, 4]:
    try:
        print max(candidates(i))
        break
    except Exception as e:
        pass

print time() - s