from math import sqrt

def form(b):
    return (-1 + sqrt(1+12*b*b-4*b)) * 0.5

lastTry = 0
def isPenta(n):
    global lastTry
    while True:
        lastTry += 1
        res = lastTry*(2*lastTry-1)
        if res == n: return True
        if res > n: return False

b, found = 2, 0

while found < 2:
    b += 1
    p = form(b)
    if int(p) == p:
        tr = p*(p+1)*0.5
        if isPenta(tr):
            found += 1

print int(tr)