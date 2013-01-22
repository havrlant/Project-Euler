def smallestMultiple(n):
    lst = range(11, n)
    x = n
    while True:
        for i in lst:
            if x % i != 0:
                break
        else:
            return x
        x += n

# print smallestMultiple(20)