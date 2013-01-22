def sumSquareDiff(n):
    sumOfSquares = sum(x * x for x in xrange(1, n + 1))
    squareOfSum = sum(xrange(1, n + 1)) ** 2
    return squareOfSum - sumOfSquares

# print sumSquareDiff(100)