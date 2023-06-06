LIMIT = 100

square_of_sum = ((LIMIT * (LIMIT + 1)) // 2) ** 2
sum_of_square = (LIMIT * (LIMIT + 1) * ((2 * LIMIT) + 1)) // 6
print(square_of_sum - sum_of_square) # 25164150