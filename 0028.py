SIZE = 1001
ne_diag, nw_diag, se_diag, sw_diag = 0, 0, 0, 0
for i in range(1, (SIZE // 2) + 1):
    ne_diag += (4 * i * i) + (4 * i) + 1
    nw_diag += (4 * i * i) + (2 * i) + 1
    se_diag += (4 * i * i) - (2 * i) + 1
    sw_diag += (4 * i * i) + 1
print(ne_diag + nw_diag + se_diag + sw_diag + 1) # 669171001