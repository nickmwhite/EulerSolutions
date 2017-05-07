max = 100
## sum of squares
sum_list = []
for i in range(max+1):
    sum_list.append(i ** 2)
sum_of_squares = sum(sum_list)

## square of sums
square_list = []
for i in range(max+1):
    square_list.append(i)
square_of_sums = sum(square_list) ** 2

## difference
difference = square_of_sums - sum_of_squares
print sum_of_squares
print square_of_sums
print difference
