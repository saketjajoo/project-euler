def validate_fraction(nr, dr):
    if (nr % 10 == 0) and (dr % 10 == 0):
        return False
    common, val = False, 0
    for ch in str(nr):
        if ch in str(dr):
            common = True
            val = ch
            break
    if not common:
        return False
    new_nr = int(str(nr).replace(val, '', 1))
    new_dr = int(str(dr).replace(val, '', 1))
    try:
        if (nr / dr) == (new_nr / new_dr):
            return True
    except Exception as e:
        # print(f'{nr}/{dr}   --   {new_nr}/{new_dr}')
        pass
    return False
    

fractions = []
for i in range(10, 100):
    for j in range(i + 1, 100):
        if validate_fraction(i, j) is True:
            fractions.append((i, j))
print(fractions) # [(16, 64), (19, 95), (26, 65), (49, 98)]
# answer = 100