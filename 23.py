import math


def is_abundant(n):
    s = 1
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            s += i
            if i != n / i:
                s += n / i
    return s > n


# Array to mark abundant numbers (up to 28123)
abundant_flags = [False] * 28124

for i in range(1, len(abundant_flags)):  # Start from 1, as 0 is not considered
    if is_abundant(i):
        abundant_flags[i] = True

abundant_list = []
for i in range(len(abundant_flags)):
    if abundant_flags[i]:
        abundant_list.append(i)

# Array to mark sums (up to 56246)
sum_of_two_abundants = [False] * (28123 * 2 + 1)

for i_val in abundant_list:
    for j_val in abundant_list:
        current_sum = i_val + j_val
        if current_sum < len(sum_of_two_abundants):
            sum_of_two_abundants[current_sum] = True

total_sum = 0
for i in range(1, 28124):  # Iterate from 1 up to 28123 (inclusive)
    if not sum_of_two_abundants[i]:
        total_sum += i

print(total_sum)
