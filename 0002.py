LIMIT = 4000000
fibonacci_list = [0, 1]
i, j = 0, 1
while True:
    element = fibonacci_list[i] + fibonacci_list[j]
    if element >= LIMIT:
        break
    fibonacci_list.append(element)
    i += 1
    j += 1

result = 0
for i in range(len(fibonacci_list)):
    if fibonacci_list[i] % 2 == 0:
        result += fibonacci_list[i]
print(result) # 4613732