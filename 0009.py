for i in range(1, 1001):
    for j in range(i + 1, 1001):
        k = 1000 - i - j
        if i < j < k:
            if (i ** 2) + (j ** 2) == (k ** 2):
                print(i * j * k) # 31875000
                exit(0)