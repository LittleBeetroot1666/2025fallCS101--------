def kpj(listy):
    return ' '.join(listy)


n = int(input())
if n % 2 == 1:
    print(-1)
else:
    js = [str(n - i) for i in range(n)]
    print(kpj(js))
