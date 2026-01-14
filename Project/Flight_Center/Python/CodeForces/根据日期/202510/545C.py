n = int(input())
trees = []
for i in range(n):
    th = list(map(int, input().split()))
    trees.append(th)

if n <= 2:
    cut = n
else:
    cut = 2
    left = trees[0][0]
    for i in range(1, n - 1):
        if trees[i][0] - trees[i][1] > left:
            cut += 1
            left = trees[i][0]
        elif trees[i][0] - trees[i][1] <= left and trees[i][0] + trees[i][1] < trees[i + 1][0]:
            cut += 1
            left = trees[i][0] + trees[i][1]
        else:
            cut += 0
            left = trees[i][0]

print(cut)
