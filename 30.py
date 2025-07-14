import math

pow4 = [i**5 for i in range(10)]

res = 0
for i in range(10, 1000000):
    num = str(i)
    sum = 0
    for n in num:
        sum += pow4[int(n)]
    if sum == i:
        res += i
print(res)
