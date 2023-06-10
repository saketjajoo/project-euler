import utils

LIMIT = 1000000
result = 0
for i in range(1, LIMIT):
    if utils.is_palindrome(i) and utils.is_palindrome(str(bin(i))[2:].lstrip('0')):
        result += i
print(result) # 872187