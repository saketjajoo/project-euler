import utils

def get_num_of_primes(a, b):
    n = 0
    while True:
        soln = (n * n) + (a * n) + b
        if soln > 0:
            if not utils.is_prime(soln):
                return n
        else:
            return n
        n += 1

all_primes = utils.sieve_of_eratosthenes(1000)
max_num_of_primes = 0
coeff = [None, None]
for a in range(-999, 1001, 2):
    for b in all_primes:
        num_of_primes = get_num_of_primes(a, b)
        if num_of_primes > max_num_of_primes:
            max_num_of_primes = num_of_primes
            coeff = [a, b]
print(coeff[0] * coeff[1]) # -59231