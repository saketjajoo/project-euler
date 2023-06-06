import utils

LIMIT = 2000000
sieve = utils.sieve_of_eratosthenes(LIMIT)
result = 0
for i in range(2, len(sieve)):
    if sieve[i]:
        result += i
print(result) # 142913828922