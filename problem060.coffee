euler = require "euler"
prelude = require "prelude"


concatNumbers = (a, b) -> 
    euler.digitsToNumber(euler.digits(a).concat euler.digits(b))

checkPrimes = (candidates) ->
    combs = euler.combinations candidates, 2
    prelude.all (([a,b]) -> (euler.isPrime concatNumbers a, b) and (euler.isPrime concatNumbers b, a)), combs

primes = [2, 3, 5]

for i in [6..1000]
    if euler.isPrime i
        combs = euler.combinations primes, 3
        for c in combs
            if checkPrimes c.concat [i]
                console.log (c.concat [i])
        primes.push i

# console.log checkPrimes [3, 7, 109, 673]