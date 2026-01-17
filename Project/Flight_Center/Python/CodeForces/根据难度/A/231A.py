n = int(input())
cooperate = 0
for t in range(n):
    i, j, k = map(int, input().split())
    s = i + j + k
    if s >= 2:
        cooperate = cooperate + 1
print(cooperate)
