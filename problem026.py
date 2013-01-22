def getRecur(upto):
    div = 100 ** 10
    for i in xrange(1, upto):
        temp = div / i
        if temp * i != div:
            yield i

print len(list(getRecur(1000)))