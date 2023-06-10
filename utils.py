import math, itertools

def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def get_all_prime_factors(x):
    prime_factors = []
    for i in range(2, int(math.sqrt(x))):
        if x % i == 0:
            if is_prime(i):
                prime_factors.append(i)
            if is_prime(int(x / i)):
                prime_factors.append(i)
    return prime_factors

def is_palindrome(x):
    return str(x)[::] == str(x)[::-1]

def get_lcm(x):
    lcm = 1
    for i in x:
        lcm = lcm * i // math.gcd(lcm, i)
    return lcm

def sieve_of_eratosthenes(n):
    sieve = [True] * n
    for p in range(2, n):
        if sieve[p]:
            for i in range(p * p, n, p):
                sieve[i] = False
    prime_numbers = []
    for i in range(len(sieve)):
        if sieve[i] is True:
            prime_numbers.append(i)
    return prime_numbers[2:]

def get_num_of_factors(n):
    return sum(2 for i in range(1, round(math.sqrt(n) + 1)) if not n % i)

def get_divisors(n):
    divs = [1]
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divs.extend([i, n // i])
    divs.extend([n])
    return sorted(list(set(divs)))

def get_all_permutations(l, fixed_len = True):
    if fixed_len is True:
        return list(itertools.permutations(l))
    else:
        permutations = []
        for i in range(1, len(l) + 1):
            permutations.extend(list(itertools.permutations(l, i)))
        return permutations

def get_triangle_numbers(n):
    result = []
    for i in range(1, n + 1):
        result.append((i * (i + 1)) // 2)
    return result