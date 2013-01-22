powers = {str(a):a**5 for a in xrange(11)}
print sum(n for n in xrange(10, 9**5 * 6) if sum(powers[x] for x in str(n)) == n)