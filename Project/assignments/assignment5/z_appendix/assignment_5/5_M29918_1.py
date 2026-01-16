# Time Limit Exceeded
t = int(input())
n = [0]
for i in range(2,100001):
    d = 0
    for j in range(1,int(i**0.5)+1):
        if i % j == 0:
            if j ** 2 == i or j == 1:
                d += j
            else:
                d += j + i // j
    n.append(d)
for i in range(2,100001):
    if n[i-1] > 99999:
        continue
    elif n[n[i-1]-1]== i:
        if i < n[i-1] <= t:
            print(i,n[i-1])
