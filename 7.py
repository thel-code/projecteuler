import math

limit = 1000000

sive = [True] * limit
sive[0] = sive[1] = False

for k in range(2, int(math.sqrt(limit)) + 1):
    if sive[k]:
        for i in range(k*k, limit, k):
            sive[i] = False

nr = 10001
for i in range(len(sive)):
    if sive[i]:
        nr -= 1
    if nr == 0:
        print(i)
        break
