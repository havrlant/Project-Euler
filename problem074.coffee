euler = require "euler"

next = (n, factorials) ->
	euler.digits(n).map((i) -> factorials[i]).reduce(((a, b) -> a + b), 0)

chainLength = (n, nextNumbers, factorials) ->
	visited = [n]
	while 1
		nextNumbers[n] = next n, factorials if not nextNumbers[n]
		num = nextNumbers[n]
		return visited.length if num in visited
		visited.push num
		n = num

combinationCount = (k, n, factorials) ->
    return factorials[n] / (factorials[n - k] * factorials[k])

permutationsCount = (counter, length, factorials) ->
    temp = 1
    for k, v of counter
        temp *= combinationCount v, length, factorials
        length -= v
    temp

nextNumbers = {}
factorials = (euler.factorial i for i in [0..9])
digits = [1,2,3,4,5,6,7,8,9]

sum = 0
for i in [1..6]
	combs = euler.repcombinations digits, i
	for c in combs when chainLength(euler.digitsToNumber(c), nextNumbers, factorials) == 60
		perms = permutationsCount (euler.counter c), c.length, factorials
		sum += perms + ((perms * 3/4) * (1 in c))

console.log sum