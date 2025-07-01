import math

n = 600851475143
limit = int(math.sqrt(n)) + 1

sive = [True] * limit
sive[0] = sive[1] = False

for k in range(2, int(math.sqrt(limit)) + 1):
    if sive[k]:
        for i in range(k*k, limit, k):
            sive[i] = False

res = 1

for i in range(len(sive)):
    if sive[i]:
        if n % i == 0:
            res = i

print(res)
