n = int(input())
print(' '.join([str(((i ** 2 + 3 * i) // 2 + 1) % n + 1) for i in range(n - 1)]))
