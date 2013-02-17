prel = require "prelude"

digits = (num) -> 
    list = []
    while num > 0
        list.push num % 10
        num = Math.floor(num / 10)
    list

sameDigits = (dig1, dig2) ->
    dig2.sort()
    prel.all ((i) -> dig1[i] == dig2[i]), [0..dig1.length - 1]

checkDigits = (i, x, baseDigits) ->
    sameDigits baseDigits, digits i * x

findSmallest = () ->
    i = 9
    while true
        i++
        baseDigits = digits i
        if baseDigits[baseDigits.length - 2] == 7
            i += Math.pow(10, baseDigits.length) - i
            continue
        baseDigits.sort()
        if prel.all ((x) -> checkDigits i, x, baseDigits), [2..6]
            return i

console.log findSmallest()