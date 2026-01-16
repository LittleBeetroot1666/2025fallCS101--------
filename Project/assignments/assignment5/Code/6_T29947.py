n,line = list(map(int, input().split()))
tree = n + 1
cut = []
for _ in range(line):
    a,b = list(map(int, input().split()))
    cut.append((a,b))
cut.sort(key=lambda x:x[0])

init = 0
kil = 0
while init <= line-1:
    at = cut[init][0]
    bt = cut[init][1]
    while init < line-1 and cut[init+1][0] <= bt:
         init += 1
         bt = max(cut[init][1], cut[init-1][1],bt)
    init += 1
    kil += bt - at + 1

print(tree - kil)
