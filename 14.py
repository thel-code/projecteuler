def col(n, count=1):
    if (n == 1):
        return count
    elif (n % 2 == 0):
        return col(int(n/2), count + 1)
    else:
        return col(3 * n + 1, count + 1)


max = -1
max_nr = -1

for i in range(1, 1000000):
    cur = col(i)
    if cur > max:
        max = cur
        max_nr = i

print(max_nr)
