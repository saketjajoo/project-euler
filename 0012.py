from collections import Counter
import utils

n = 1
while True:
    triangle_number = (n * (n + 1)) // 2
    if utils.get_num_of_factors(triangle_number) >= 500:
        print(triangle_number) # 76576500
        break
    n += 1