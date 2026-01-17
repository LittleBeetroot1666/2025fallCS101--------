n, x = list(map(int, input().split()))
js = list(map(int, input().split()))
sgm = abs(sum(js)) + x - 1
print(sgm // x)
