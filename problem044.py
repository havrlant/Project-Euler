def Pn(n):
    return (n*(3*n-1)) / 2

numbers = [Pn(x) for x in xrange(1, 3000)]
hashNumbers = set(numbers)

candidates = set()
for a in numbers:
    for b in numbers:
        if b == a:
            break
        if a+b in hashNumbers and a-b in hashNumbers:
            candidates.add(abs(a-b))
print min(candidates)