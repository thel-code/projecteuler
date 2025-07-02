sive = [True] * 2000000

for i in range(2, len(sive)):
    if sive[i]:
        k = 2
        while (i * k < len(sive)):
            sive[i*k] = False
            k += 1

res = 0
for i in range(2, len(sive)):
    if sive[i]:
        res += i
print(res)
