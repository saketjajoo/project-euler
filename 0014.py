seen = {}

def build_chain(n):
    N = n
    chain = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            if seen.get(n):
                chain.extend(seen[n])
                break
            else:
                chain.append(n)
        else:
            n = (3 * n) + 1
            if seen.get(n):
                chain.extend(seen[n])
                break
            else:
                chain.append(n)
    seen[N] = chain
    return len(chain)

n = 1
result, max_chain_length = None, 0
while n <= 1000000:
    chain_length = build_chain(n)
    if chain_length > max_chain_length:
        max_chain_length = chain_length
        result = n
    n += 1
print(result) # 837799