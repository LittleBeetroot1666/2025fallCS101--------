for _ in range(int(input())):
    n, a = list(map(int, input().split()))
    js = list(map(int, input().split()))
    js.sort()
    js1 = []
    js2 = []
    for j in js:
        if j < a:
            js1.append(j)
        elif j > a:
            js2.append(j)
    if len(js1) < len(js2):
        print(a + 1)
    else:
        print(a - 1)
