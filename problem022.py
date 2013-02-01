with open('names.txt', 'r') as f:
    names = sorted(f.read().replace('"', '').split(","))

print sum(i * sum(ord(x) - 64 for x in name) for i, name in enumerate(names, 1))