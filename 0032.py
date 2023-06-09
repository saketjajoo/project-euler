result, seen = 0, set()
for a in range(9, 99):
    for b in range(98, 987):
        c = a * b
        if len(str(c)) > 5:
            break
        if sorted(str(c) + str(a) + str(b)) == list('123456789'):
            if c not in seen :
                seen.add(c)
                result += c

for a in range(1,10):
    for b in range(987,9877):
        c = a * b
        if len(str(c)) > 5:
            break
        if sorted(str(c) + str(a) + str(b)) == list('123456789'):
            if c not in seen :
                seen.add(c)
                result += c
print(result) # 45228