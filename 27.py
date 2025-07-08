import math


sive = [True] * 1_000_000_000

limit = math.sqrt(len(sive))
for i in range(limit):
    if sive[i]:
        k = 2
        while i + k * i < len(sive):
            sive[i + k * i] = True
            k += 1
