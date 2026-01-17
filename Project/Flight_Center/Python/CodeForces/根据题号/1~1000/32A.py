n, d = list(map(int, input().split()))
js = list(map(int, input().split()))
cnt = 0
for i in js:
    for j in js:
        if abs(i - j) <= d:
            cnt += 1
cnt -= len(js)
print(cnt)
