a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))
e = list(map(int, input().split()))
if c[2] == 1:
    print(0)
elif b[2] == 1 or c[1] == 1 or c[3] == 1 or d[2] == 1:
    print(1)
elif a[2] == 1 or b[1] == 1 or b[3] == 1 or c[0] == 1 or c[4] == 1 or d[1] == 1 or d[3] == 1 or e[2] == 1:
    print(2)
elif a[0] == 1 or a[4] == 1 or e[0] == 1 or e[4] == 1:
    print(4)
else:
    print(3)
