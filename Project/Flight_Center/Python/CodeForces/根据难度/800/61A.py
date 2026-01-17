a0 = input()
b0 = input()
l0 = len(a0)
a = int(a0, 2)
b = int(b0, 2)
rr = str(bin(a ^ b)[2:])
lr = len(rr)
res = '0' * (l0 - lr) + rr
print(res)
