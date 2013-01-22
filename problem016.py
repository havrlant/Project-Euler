import math

def powerDigitSum(n = 1000):
    return sum(int(x) for x in str(int(math.pow(2, n))))

# print powerDigitSum()