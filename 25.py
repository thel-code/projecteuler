import math
fib = []

fib.append(1)
fib.append(1)

i = 2
while True:
    fib.append(fib[i - 1] + fib[i - 2])
    if len(str(fib[i])) >= 1000:
        print(i + 1)
        break
    i += 1
