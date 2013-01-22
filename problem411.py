def getStations(n):
    stations = set()
    for i in xrange(0, 2*n+1):
        stations.add((2**i % n, 3**i % n))
    return stations

def isLower((a, b), (c, d)):
    return b <= d

def isLefter((a, b), (c, d)):
    return a <= c

def isValidTarget(start, station):
    return isLower(start, station) and isLefter(start, station)

def findNext(stations, score):
    generator = ((k,v) for k,v in score.iteritems() if k in stations)
    return max(generator, key=lambda x: x[1])[0]

def findRoute(stations, nextValid, score):
    s = 0
    while stations:
        s += 1
        next = findNext(stations, score)
        stations = nextValid[next]
    return s

def findOptimalPath(n):
    stations = getStations(n)
    nextValid, score = {}, {}

    for st in stations:
        next = {x for x in stations if isLower(st, x) and isLefter(st, x) and x != st}
        nextValid[st] = next
        score[st] = len(next)

    return findRoute(stations, nextValid, score)



print findOptimalPath(7**5)