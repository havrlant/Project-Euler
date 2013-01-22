import math
import time
import operator

def triangular():
    temp, i = 1, 2
    while True:
        yield temp
        temp += i
        i += 1

def divCount(num):
    sqrt = math.sqrt(num)
    return 2 * sum(1 for x in xrange(1, int(sqrt)) if num % x == 0) + int(sqrt == int(sqrt))


s = time.time()

for tr in triangular():
    dc = divCount(tr)
    if dc > 500:
        print dc, tr
        break

print time.time() - s

# print optDivCount(10)

# 576 76576500
# 6.25411701202
# [Finished in 6.3s]