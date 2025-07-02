import math


def get_divisor_count(nr):
    divisors = 0
    for i in range(1, int(math.sqrt(nr)) + 1):
        if nr % i == 0:
            divisors += 2
    return divisors


print(get_divisor_count(28))

sum = 0
for i in range(100000):
    sum += i
    if get_divisor_count(sum) >= 500:
        print(sum)
