def getDigits(n):
    digits = []
    while n > 0:
        residue = n % 10
        n /= 10
        digits.append(residue)
    return tuple(reversed(digits))

codes = map(lambda x: tuple(map(int, str(x))), '319 680 180 690 129 620 762 689 762 318 368 710 720 710 629 168 160 689 716 731 736 729 316 729 729 710 769 290 719 680 318 389 162 289 162 718 729 319 790 680 890 362 319 760 316 729 380 319 728 716'.split(' '))

def getNext(found):
    for x in xrange(10):
        if x in found: continue
        for a,b,c in codes:
            if x in {b,c}:
                if not((a in found) and ((b == x) or (b in found))):
                    break
        else:
            yield x

found = [4,5]

while 1:
    next = list(getNext(found))
    if len(next) == 1:
        found.append(next[0])
    else:
        break

print "".join(map(str, found[2:]))