import time

def next(n):
    return int(n / 2) if n % 2 == 0 else 3 * n + 1

cache = {1 : 1}

def getChain(n):
    orig, count = n, 0

    while True:
        if n in cache:
            break
        count += 1
        n = next(n)

    totalLength = count + cache[n]
    cache[orig] = totalLength
    return totalLength

s = time.time()
generator = ((getChain(x), x) for x in xrange(1, 1000000))
print max(generator, key = lambda x: x[0])
print time.time() - s