import utils

permutations = utils.get_all_permutations(list(range(0, 10)))
print(''.join(list(map(str, permutations[999999])))) # 2783915460