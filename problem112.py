from euler import num_to_digits

def is_bouncy(n):
	digits = num_to_digits(n)
	return not (is_increasing(digits) or is_increasing(reversed(digits)))

def is_increasing(digits):
	last = -1
	for d in digits:
		if d >= last:
			last = d
		else:
			return False
	return True

def naturals():
	i = 1
	while True:
		yield i
		i += 1

bounced = 0

for i in naturals():
	if is_bouncy(i):
		bounced += 1
	if bounced / float(i) == 0.99:
		print i
		break