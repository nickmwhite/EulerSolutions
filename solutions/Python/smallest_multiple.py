counter = 20
multiples = 10
remainders = []
while sum(remainders) != 0:
    for i in range(1,multiples + 1):
        remainders.append(counter % i)
    counter += 1
print counter
