def pythagoreanTriplet():
    for c in xrange(334, 1001):
        for b in xrange((1001 - c) / 2 + 1, min(c, 999 - c)):
            a = 1000 - c - b
            if a ** 2 + b ** 2 == c ** 2:
                return a, b, c

# print pythagoreanTriplet()