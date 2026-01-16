def sgm_skin(amatrix):
    if len(amatrix) == 1:
        return amatrix[0][0]
    elif len(amatrix) == 2:
        return amatrix[0][0] + amatrix[0][1] + amatrix[1][0] + amatrix[1][1]
    else:
        k0 = 0
        k0 += sum(amatrix[0])
        k0 += sum(amatrix[-1])
        for _ in range(1, len(amatrix) - 1):
            k0 += amatrix[_][0]
            k0 += amatrix[_][-1]
        return k0

def peel(amatrix):
    if len(amatrix) <= 2:
        return [[]]
    elif len(amatrix) == 3:
        return [[amatrix[1][1]]]
    else:
        new_amatrix = []
        for _ in range(1, len(amatrix) - 1):
            new_amatrix.append(amatrix[_][1:len(amatrix[_]) - 1])
        return new_amatrix


n = int(input())
js = []
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
js.append(sgm_skin(matrix))
for j in range((n - 1)//2):
    matrix = peel(matrix)
    js.append(sgm_skin(matrix))

print(max(js))
