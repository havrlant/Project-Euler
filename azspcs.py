from math import factorial
from itertools import combinations_with_replacement, ifilter


def filterSeqs(contains, seqs):
    maxC = max(contains)
    newSeq = {x for x in seqs if max(x) <= maxC}
    newSeq = sorted(newSeq, key=lambda x: max(x), reverse=True)[:250]
    return newSeq

def sequence(contains, seqs):
    newSeqs = set()

    for seq in seqs:
        if contains < seq:
            return seq

    seqs = filterSeqs(contains, seqs)
    print len(seqs)
    for seq in seqs:
        candidates = getAllCombs(seq)
        for cand in candidates:
            newSeqs.add(frozenset(seq | {cand}))

    return sequence(contains, newSeqs)


def getAllCombs(seq):
    def allCombs():
        for a, b in combinations_with_replacement(seq, 2):
            yield a+b
            yield a*b
            # yield a-b
            # yield b-a
    return set(ifilter(lambda x: x not in seq and x != 0, allCombs()))

print sequence({13*12*11*10, 9*8*7*6, 5*4*3*2}, [frozenset((1, 2))])
# print set(getAllCombs([1, 2]))