import math


def d(n):
    if n == 0:
        return 0
    res = 1
    for i in range(2, int(math.sqrt(n))):
        if (n % i == 0):
            res += i
            res += n/i
    return int(res)


s = set()
for a in range(10000):
    b = d(a)
    db = d(b)
    if db == a and a != b:
        s.add(a)
        s.add(b)
print(sum(s))
