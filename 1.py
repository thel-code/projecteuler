max = 1000
res = 0

for i in range(max):
    if i % 3 == 0 or i % 5 == 0:
        res += i

print(res)
