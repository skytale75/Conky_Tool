a = 1
b = 2

evens = [ 2 ]

while a + b < 4000000:
    a = a + b
    b = a + b
    if a % 2 == 0:
        evens.append(a)
    if b % 2 == 0:
        evens.append(b)

print(b, len(evens), sum(evens))