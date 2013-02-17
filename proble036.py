def getBinaryNumbers(length):
    for i in xrange(2**length):
        yield bin(i)[2:].zfill(length)

def getBinPal(length):
    if length % 2 == 0:
        for comb in getBinaryNumbers(int(length / 2)):
            yield comb + "".join(reversed(comb))
    else:
        for comb in getBinaryNumbers(int((length + 1) / 2)):
            yield comb + "".join(reversed(comb[:-1]))

def binaryPalindromes():
    yield 1
    yield 3
    for i in xrange(1, 19):
        for binpal in getBinPal(i):
            yield int('1' + binpal + '1', 2)

def isPalindrome(n):
    s = str(n)
    slen = len(s)
    for i in xrange(slen / 2):
        if s[i] != s[slen - i - 1]:
            return False
    return True

print sum(x for x in binaryPalindromes() if isPalindrome(x) and x < 1000000)