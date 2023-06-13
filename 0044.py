def generate_pentagonal_numbers(n):
    pentagonal_numbers = []
    for i in range(1, n + 1):
        pentagonal_numbers.append((i * ((3 * i) - 1)) // 2)
    return pentagonal_numbers

pentagonal_numbers = generate_pentagonal_numbers(10000)
pentagonal_numbers_set = set(pentagonal_numbers)

minimum_difference = float('inf')
for i in range(len(pentagonal_numbers)):
    for j in range(i + 1, len(pentagonal_numbers)):
        if (pentagonal_numbers[i] + pentagonal_numbers[j] in pentagonal_numbers_set) and (abs(pentagonal_numbers[i] - pentagonal_numbers[j]) in pentagonal_numbers_set):
            minimum_difference = min(minimum_difference, abs(pentagonal_numbers[i] - pentagonal_numbers[j]))
print(minimum_difference) # 5482660