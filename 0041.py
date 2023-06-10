import utils

result = 0
for i in range(1, 10):
    print(i)
    all_permutations = utils.get_all_permutations([j for j in range(1, i + 1)])
    for permutation in all_permutations:
        number = int(''.join(list(map(str, permutation))))
        if utils.is_prime(number):
            result = max(result, number)
print(result) # 7652413