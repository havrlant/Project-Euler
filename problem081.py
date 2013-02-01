with open('matrix.txt', 'r') as f:
    matrix = map(lambda x: map(int, x.split(',')), f.read().splitlines())

for i in xrange(79):
    matrix[0][i+1]+=matrix[0][i]
    matrix[i+1][0]+=matrix[i][0]

for i in xrange(1, 80):
    for j in xrange(1, 80):
        matrix[i][j] += min(matrix[i-1][j], matrix[i][j-1])

print matrix[79][79]