def pandigital(num):
    concatenated_result = ''
    i = 1
    while True:
        concatenated_result +=str(num * i)
        if len(concatenated_result) >= 9:
            break
        i += 1
    if len(concatenated_result) != 9:
        return False, None
    if ''.join(sorted(concatenated_result)) == '123456789':
        return True, int(concatenated_result)
    return False, None

result = 0
for i in range(10, 10000):
    is_pandigital, pandigital_num = pandigital(i)
    if is_pandigital is True:
        result = max(result, pandigital_num)
print(result) # 932718654