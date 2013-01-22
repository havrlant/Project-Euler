#!/opt/local/bin/python
from euler import fib
from itertools import dropwhile

print dropwhile(lambda (a, b): len(str(b)) < 1000, enumerate(fib())).next()[0]