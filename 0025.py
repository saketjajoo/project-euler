index = 3
a, b = 1, 2
while True:
    next_fibo = a + b
    index += 1
    if len(str(next_fibo)) == 1000:
        print(index) # 4782
        break
    a, b = b, next_fibo