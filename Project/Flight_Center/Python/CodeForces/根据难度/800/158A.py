s = 0
n, k = list(map(int, input().split()))
a_s = list(map(int, input().split()))
for i in range(n):
    if a_s[i] >= a_s[k-1] and a_s[i]>0:
        s += 1
print(s)
