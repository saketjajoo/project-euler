import utils

LIMIT = 10000
all_primes = utils.sieve_of_eratosthenes(LIMIT)
result = 0
seen = []
for i in range(2, LIMIT):
    if i not in all_primes and i not in seen:
        d_a = sum(utils.get_divisors(i)[0: -1])
        d_b = sum(utils.get_divisors(d_a)[0: -1])
        seen.extend([d_a, d_b])
        if i == d_b and d_a != d_b:
            result += i + d_a
print(result) # 31626