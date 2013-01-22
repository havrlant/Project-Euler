def multiplesOf35(n):
    return sum(x for x in xrange(1, n) if x % 3 == 0 or x % 5 == 0)

# print multiplesOf35(1000)