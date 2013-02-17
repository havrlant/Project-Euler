fs = require 'fs'

log = ([a, x]) -> 
    x * Math.log a

numbers = (pair) -> 
    pair.split(',').map((x) -> parseInt(x, 10))

findMax = (pairs) ->
    [max, index] = [0, 0]
    for pair, i in pairs.split('\n')
        l = log(numbers(pair))
        if l > max
            max = l
            index = i
    console.log max, index + 1

fs.readFile('base_exp.txt', (err, data) -> findMax data.toString())