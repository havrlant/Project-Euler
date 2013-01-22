from itertools import permutations, islice

for i, perm in enumerate(permutations('0123456789'), 1):
    if i == 1000000:
        print "".join(perm)

# print "".join(islice(permutations('0123456789'), 999999, 1000000).next())

# 2783915460