starie = 1
n = int(input())
js = list(map(int, input().split()))
sgm = 0
sgm += starie
j = 1
while j < len(js):
    if js[j] != js[j - 1] and j != 1:
        starie = 0
    if js[j] == js[j - 1]:
        starie = 1
        sgm += starie
        j += 1
    elif js[j] < js[j - 1]:
        while j < len(js) and js[j] < js[j - 1]:
            starie += 1
            sgm += starie
            j += 1
    else:
        while j < len(js) and js[j] > js[j - 1]:
            starie += 1
            sgm += starie
            j += 1
print(sgm)
