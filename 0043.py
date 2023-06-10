import utils

divisors = [2, 3, 5, 7, 11, 13, 17]

def satisfies_property(number):
    number = str(number)
    for digit_index in range(1, 8):
        sub_number = number[digit_index : digit_index + 3]
        if int(sub_number) % divisors[digit_index - 1] != 0:
            return False
    return True

all_permutations = utils.get_all_permutations([i for i in range(0, 10)])
result = 0
for i in range(len(all_permutations)):
    pandigital_number = int(''.join(list(map(str, all_permutations[i]))))
    if satisfies_property(pandigital_number):
        result += pandigital_number
print(result) # 16695334890