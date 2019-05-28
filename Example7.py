import random

b = []

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
while len(b) < 7:
    b.append(a[random.randint(0,9)])

print(b)
