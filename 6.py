sum = (100*(100+1))/2
sum = sum ** 2

for i in range(101):
    sum -= i**2
print(sum)
