def check_sum(num):
    _sum = 0
    for digit in str(num):
        _sum += int(digit) ** 5
    if _sum == num:
        return True
    return False

result = 0
for i in range(10, 500000):
    if check_sum(i) is True:
        result += i
print(result) # 443839