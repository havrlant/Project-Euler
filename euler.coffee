exports.digits = (num) -> 
    list = []
    while num > 0
        list.push num % 10
        num = Math.floor(num / 10)
    list.reverse()

exports.isPalindrome = (digits) ->
    len = digits.length
    for i in [0..Math.floor(len / 2)] when digits[i] != digits[len - i - 1]
        return false
    return true

exports.digitsToNumber = (digits) -> 
    sum = 0
    for d in digits
        sum *= 10
        sum += d
    sum

exports.isPrime = (n) ->
    if n < 2 then return false
    if n == 2 then return true
    if n % 2 == 0 then return false
    for i in [3..Math.floor(Math.sqrt(n))] by 2
        if n % i == 0
            return false
    return true

exports.combinations = (list, n) ->
    combs = combinations list.length, n
    for indices in combs
        for i in indices
            list[i]

exports.repcombinations = (arr, k) ->
    return [ [] ] if k == 0
    return [] if arr.length == 0
   
    combos_with_head = ([arr[0]].concat combo for combo in exports.repcombinations arr, k-1)
    combos_sans_head = exports.repcombinations arr[1...], k
    combos_with_head.concat combos_sans_head

exports.factorial = (n) -> 
    if n > 0 then n * exports.factorial(n - 1) else 1

exports.counter = (list) ->
    sums = {}
    for x in list
        sums[x] = (if sums[x] then sums[x] + 1 else 1)
    sums

clone = (arr) -> (n for n in arr)

combinations = (n, p) ->
  return [ [] ] if p == 0
  i = 0
  combos = []
  combo = []
  while combo.length < p
    if i < n
      combo.push i
      i += 1
    else
      break if combo.length == 0
      i = combo.pop() + 1
 
    if combo.length == p
      combos.push clone combo
      i = combo.pop() + 1
  combos