import utils

def is_abundant(n):
    return sum(utils.get_divisors(n)[0: -1]) > n

abundant_nums = [i for i in range(12, 28124) if is_abundant(i)]
abundant_sums = set([])
for i in abundant_nums:
    for j in abundant_nums:
        if (i + j) > 28123:
            break
        else:
            abundant_sums.add(i + j)
result = [number for number in range(28124) if number not in abundant_sums]
print(sum(result)) # 4179871