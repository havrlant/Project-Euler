from time import time

def isPalindrome(n):
    s = str(n)
    for i in xrange(len(s) / 2):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True

s = time()
print max(x*y for x in xrange(100, 1000) for y in xrange(100, 1000) if isPalindrome(x*y))
print time() - s