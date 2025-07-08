import math


sive = [True] * 10_000_000

limit = int(math.sqrt(len(sive)) + 1)
for i in range(2, limit):
    if sive[i]:
        for j in range(i * i, len(sive), i):
            sive[j] = False

a_max = -1001
b_max = -1001
n_max = -1
for a in range(-1000, 1000):
    for b in range(-1000, 1000):
        n = 0
        while True:
            res = n*n + a * n + b
            if res < 0 or not sive[res]:
                break
            n += 1
        if n > n_max:
            print(a)
            print(b)
            n_max = n
            b_max = b
            a_max = a
print(a_max * b_max)
