def kpj(strry_listy):
    return ' '.join(strry_listy)


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    if m == 1:
        for i in range(n + 1):
            print(0)
    else:
        if n == m:
            print(n)
            for t in range(n):
                if t < n-1:
                    numbers = list(i % n for i in range(t+1, t+n+1))
                    numbers = map(str, numbers)
                else:
                    numbers = list(range(1, n))+[0]
                    numbers = map(str, numbers)
                print(kpj(numbers))
        elif n < m:
            print(n+1)
            for t in range(n):
                numbers = list(i % m for i in range(t+1, t+m+1))
                numbers = map(str, numbers)
                print(kpj(numbers))
        else:
            if m == 1:
                print(0)
                for _ in range(n):
                    print(0)
            else:
                print(m)
                for t in range(n):
                    if t < m-1:
                        numbers = list(i % m for i in range(t+1, t+m+1))
                        numbers = map(str, numbers)
                    else:
                        numbers = list(range(1, m))+[0]
                        numbers = map(str, numbers)
                    print(kpj(numbers))
