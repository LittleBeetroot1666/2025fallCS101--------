x, n = list(map(int, input().split()))
js = list(map(int, input().split()))
if 1 not in js:
    print('-1')
else:
    js.sort(reverse=True)
    now_max = 0
    cnt = 0
    while now_max < x:
        for j in js:
            if j <= now_max + 1:
                now_max += j
                cnt += 1
                break
    print(cnt)
