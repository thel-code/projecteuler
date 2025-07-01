res = 0
n = 2520
while True:
    correct = True
    for i in range(1, 21):
        if n % i != 0:
            correct = False
    if correct:
        print(n)
        break
    n += 20
    print(n)
