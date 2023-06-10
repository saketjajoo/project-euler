import utils

all_primes = set(utils.sieve_of_eratosthenes(1000000))

def get_all_numbers_after_truncation(num, rev = False):
    result = []
    num = str(num)
    for i in range(1, len(num)):
        if rev:
            result.append(int((num[i:])[::-1]))
        else:
            result.append(int(num[i:]))
    return result

def check_truncatability(num):
    left_truncated_numbers = get_all_numbers_after_truncation(num)
    for i in range(len(left_truncated_numbers)):
        if left_truncated_numbers[i] not in all_primes:
            return False

    right_truncated_numbers = get_all_numbers_after_truncation(int(str(num)[::-1]), rev = True)
    for i in range(len(right_truncated_numbers)):
        if right_truncated_numbers[i] not in all_primes:
            return False
    return True

count = 0
result = 0
i = 11
while True:
    if i in all_primes:
        if check_truncatability(i) is True:
            count += 1
            result += i
    if count == 11:
        break
    i += 1
print(result) # 748317