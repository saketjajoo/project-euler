number = ''.join([str(i) for i in range(1, 200000)])
index = [10 ** i for i in range(0, 7)]
result = 1
for i in range(len(index)):
    result *= int(number[index[i] - 1])
print(result) # 210