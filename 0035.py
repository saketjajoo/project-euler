import utils

LIMIT = 1000000
all_primes = set(utils.sieve_of_eratosthenes(LIMIT))

def is_circular_prime(num):
    if num not in all_primes:
        return False
    num = str(num)
    for i in range(len(num)):
        if int(num[i:] + num[0:i]) not in all_primes:
            return False
    return True

count = 0
for i in range(2, LIMIT):
    if is_circular_prime(i):
        count += 1
print(count) # 55