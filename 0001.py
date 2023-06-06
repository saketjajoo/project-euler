LIMIT = 1000
result = 0
for i in range(3, LIMIT):
    if i % 3 == 0 or i % 5 == 0:
        result += i
print(result) # 233168