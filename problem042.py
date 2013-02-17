with open('words.txt', 'r') as f:
    words = f.read().replace('"', '').split(',')

def isTriangle(word, triangles = {int(n/2.0*(n+1)) for n in xrange(1, 30)}):
    return sum(ord(x) - 64 for x in word) in triangles

print sum(1 for x in words if isTriangle(x))