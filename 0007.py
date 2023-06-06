import utils
LIMIT = 10001
prime_count, num = 0, 1
while prime_count < LIMIT:
    num += 1
    if utils.is_prime(num):
        prime_count += 1
print(num) # 104743