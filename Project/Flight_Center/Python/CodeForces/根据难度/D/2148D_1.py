for _ in range(int(input())):
    n = int(input())
    js = list(map(int, input().split()))
    odd = []
    even = []
    total = 0
    for i in js:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    odd.sort()
    if len(odd) == 0:
        total = 0
    elif len(odd) % 2 == 1:
        for i in js:
            total += i
        loss = len(odd)//2
        for j in range(0, loss):
            total -= odd[j]
    else:
        for i in js:
            total += i
        loss = len(odd) // 2
        for j in range(0, loss):
            total -= odd[j]
    print(total)
