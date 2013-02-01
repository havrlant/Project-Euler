codes = '319 680 180 690 129 620 762 689 762 318 368 710 720 710 629 168 160 689 716 731 736 729 316 729 729 710 769 290 719 680 318 389 162 289 162 718 729 319 790 680 890 362 319 760 316 729 380 319 728 716'.split(' ')

def getNext(found):
    for x in map(str, xrange(10)):
        if x in found: continue
        for a,b,c in codes:
            if x in {b,c}:
                if not((a in found) and ((b == x) or (b in found))):
                    break
        else:
            return x

found = ['4','5']
for next in iter(lambda: getNext(found), None):
    found.append(next)

# print "".join(found[2:])