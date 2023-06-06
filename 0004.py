import utils

result = 0
for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        if utils.is_palindrome(i * j):
            result = max(result, i * j)
print(result) # 906609