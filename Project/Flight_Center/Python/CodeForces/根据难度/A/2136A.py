def tid(_a, _b):
    if _a <= _b * 2 + 2 and _b <= _a * 2 + 2:
        return True
    else:
        return False


l = int(input())
for i in range(l):
    a, b, c, d = list(map(int, input().split()))
    if tid(a, b) and tid(c-a, d-b):
        print("YES")
    else:
        print("NO")
