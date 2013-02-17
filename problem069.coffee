euler = require "euler"

gcd = (x, y) ->
	while y != 0
		z = x % y
		x = y
		y = z
	x

phi = (n) ->
	sum = 0
	for i in [1...n] when gcd(i, n) == 1
		sum++
	sum

# primes = (i for i in [1..1e6] when euler.isPrime i)

# phi = (n, primes) ->
# 	res = n
# 	for p in primes when n % p == 0
# 		if p < n then res *= (1 - 1/p) else break
# 	res = Math.floor res
	# if euler.isPrime res then res - 1 else res

# divisorsCount = (n) ->
# 	count = (if n > 1 then 2 else 1)
# 	sq = Math.sqrt(n)
# 	intsq = Math.floor(sq)
# 	for i in [2..intsq] by 1 when n % i == 0
# 		count += 2
# 	count -= 1 if sq == intsq
# 	count



# value = 0
# num = 0

# for n in [2..1e4]
# 	p = phi n, primes
# 	ratio = n/p
# 	if ratio > value
# 		value = ratio
# 		num = n
# 	if n % 1e4 == 0
# 		console.log n

# console.log num, value

for i in [2..50]
	console.log "n: #{i}, phi: #{phi(i)}"

# console.log phi 36
# console.log phi 36, primes
# console.log primes