import math
top = int(1e15)
upto = int(math.sqrt(top))

s = 0
for i in xrange(1, upto):
    count = int(upto / i)
    s += i*i*count
print s