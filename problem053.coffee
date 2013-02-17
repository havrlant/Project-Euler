factorial = (n) ->
    if n == 0 then 1 else n * factorial n - 1

factorials = (factorial x for x in [0..100])

cnr = (n, r) ->
    factorials[n] / (factorials[r] * (factorials[n-r]))

sum = 0
for n in [1..100]
    for r in [1..n] when cnr(n, r) > 1000000
        sum++

console.log sum