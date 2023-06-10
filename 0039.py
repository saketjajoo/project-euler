'''
a^2 + b^2 = c^2 = (p - a - b)^2
==> b = (p^2 - 2pa) / 2(p - a) == (int)
'''

max_count, result = 0, None
for p in range(2, 1001):
    count = 0
    for a in range(2, p):
        if ((p ** 2) - (2 * p * a)) % (2 * (p - a)) == 0:
            count += 1
    if count > max_count:
        max_count = count
        result = p
print(result) # 840