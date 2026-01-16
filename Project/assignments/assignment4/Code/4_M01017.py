pkg = 1
u = {0:0,1:5,2:3,3:1}
while pkg > 0:
    a,b,c,d,e,f = list(map(int, input().split()))
    pkg = f + e + d + (c + 3) // 4
    y = 5*d + u[c % 4]
    if b > y:
        pkg += (b - y + 8) // 9
    x = 36 * pkg - 36 * f - 25 * e - 16 * d - 9 * c - 4 * b
    if a > x:
        pkg += (a - x + 35) // 36
    if pkg > 0:
        print(pkg)
