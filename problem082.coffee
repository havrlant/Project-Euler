matrix = [[131, 673, 234, 103, 18],
[201, 96, 342, 965, 150],
[630, 803, 746, 422, 111],
[537, 699, 497, 121, 956],
[805, 732, 524, 37, 331]]


for sloupec in [1...matrix.length]
    for radek in [0...matrix.length]
        matrix[radek][sloupec] += matrix[radek][sloupec-1]
    for radek in [0...matrix.length]

console.log matrix