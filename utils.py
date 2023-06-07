import math

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
    return sieve

def get_num_of_factors(n):
    return sum(2 for i in range(1, round(math.sqrt(n) + 1)) if not n % i)