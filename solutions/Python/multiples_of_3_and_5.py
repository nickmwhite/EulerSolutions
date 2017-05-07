multiples = []
max = 1000
for i in range(max - 1):
    i += 1
    if i % 3 == 0 or i % 5 == 0:
        multiples.append(i)
print multiples
total = sum(multiples)
print total
