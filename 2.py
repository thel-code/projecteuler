fib = []

fib.append(1)
fib.append(2)

while fib[-1] + fib[-2] < 4000000:
    fib.append(fib[-1] + fib[-2])

res = 0

for e in fib:
    if e % 2 == 0:
        res += e


print(res)
