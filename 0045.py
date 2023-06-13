import math
def is_pentagonal(num):
    return 1 + math.sqrt(1 + (24 * num)) % 6 == 0

i = 145
while True:
    next_hexagonal_num = i * ((2 * i) - 1)
    print(next_hexagonal_num)
    if is_pentagonal(next_hexagonal_num):
        print(next_hexagonal_num) # 1533776805
        break
    i += 1