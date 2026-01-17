a, b = list(map(int,input().split()))
if a > b:
    t = a
else:
    t = b
if t == 1:
    print("1/1")
elif t == 2:
    print("5/6")
elif t == 3:
    print("2/3")
elif t == 4:
    print("1/2")
elif t == 5:
    print("1/3")
else:
    print("1/6")