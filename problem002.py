from itertools import *
from euler import *

def evenFibonacciNumbers(n):
    return sum(ifilter(isEven, takewhile(lambda x: x <= n, fib())))

print evenFibonacciNumbers(4000000)