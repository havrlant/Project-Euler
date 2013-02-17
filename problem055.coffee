euler = require "euler"

isLychrel = (n) ->
    tested = []
    for i in [1..50]
        digits = euler.digits n
        if euler.isPalindrome(digits) and (i > 1)
            return true
        n += euler.digitsToNumber digits.reverse()
    return false

sum = 0
for i in [1..9999] when not isLychrel i
    sum += 1
console.log sum