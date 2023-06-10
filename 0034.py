import math

LIMIT = 354294 # 6 * (9 ** 5)
factorials = {i : math.factorial(i) for i in range(0, 10)}

def is_curious_number(num):
    digit_factorial_sum = 0
    for digit in str(num):
        digit_factorial_sum += factorials[int(digit)]
    if digit_factorial_sum == num:
        return True
    return False

result = 0
for i in range(3, LIMIT):
    if is_curious_number(i):
        result += i
print(result) # 40730