def fact(n):
    return reduce(lambda a, b: a * b, xrange(1, n+1), 1)

facts = {str(x):fact(x) for x in xrange(11)}
print sum(i for i in xrange(3, fact(9) * 7) if sum(facts[x] for x in str(i)) == i)