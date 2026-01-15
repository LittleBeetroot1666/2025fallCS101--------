# Assignment #D: Mock Exam下元节

Updated 1729 GMT+8 Dec 4, 2025

2025 fall, Complied by <mark>郭旭杰、化学与分子工程学院</mark>

OpenJudge账号：25n2500011906，昵称：郭旭杰



>**说明：**
>
>1. Dec⽉考： AC2<mark>（请改为同学的通过数）</mark> 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。
>
>2. 解题与记录：对于每一个题目，请提供其解题思路（可选），并附上使用Python或C++编写的源代码（确保已在OpenJudge， Codeforces，LeetCode等平台上获得Accepted）。请将这些信息连同显示“Accepted”的截图一起填写到下方的作业模板中。（推荐使用Typora https://typoraio.cn 进行编辑，当然你也可以选择Word。）无论题目是否已通过，请标明每个题目大致花费的时间。
>
>3. 提交安排：提交时，请首先上传PDF格式的文件，并将.md或.doc格式的文件作为附件上传至右侧的“作业评论”区。确保你的Canvas账户有一个清晰可见的本人头像，提交的文件为PDF格式，并且“作业评论”区包含上传的.md或.doc附件。
> 
>4. 延迟提交：如果你预计无法在截止日期前提交作业，请提前告知具体原因。这有助于我们了解情况并可能为你提供适当的延期或其他帮助。  
>
>请按照上述指导认真准备和提交作业，以保证顺利完成课程要求。

![局部截取_20251209_013144](D:\to@ GitHub\启动\LittleBeetroot1666\启动\2025fallCS101--------\Project\assignments\assignmentD\z_appendix\局部截取_20251209_013144.png)![局部截取_20251209_013209](D:\to@ GitHub\启动\LittleBeetroot1666\启动\2025fallCS101--------\Project\assignments\assignmentD\z_appendix\局部截取_20251209_013209.png)



## 1. 题目

### E29945:神秘数字的宇宙旅行 

implementation, http://cs101.openjudge.cn/practice/29945

耗时：2min

思路：会f' ' 格式化输出，注意除号的书写、不要忘记最后输出“End”就没有问题。



代码

```python
n = int(input())
while n != 1:
    if n % 2 != 0:
        print(f'{n}*3+1={n*3+1}')
        n = n * 3 + 1
    else:
        print(f'{n}/2={n//2}')
        n = n//2
print('End')

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![局部截取_20251209_012931](D:\to@ GitHub\启动\LittleBeetroot1666\启动\2025fallCS101--------\Project\assignments\assignmentD\z_appendix\局部截取_20251209_012931.png)

![局部截取_20251209_013005](D:\to@ GitHub\启动\LittleBeetroot1666\启动\2025fallCS101--------\Project\assignments\assignmentD\z_appendix\局部截取_20251209_013005.png)



### E29946:删数问题

monotonic stack, greedy, http://cs101.openjudge.cn/practice/29946

耗时：3h

思路：使用单调栈，后一个数字比前一个数字大就从栈顶弹出，直至用完所有次数找到最小的数。



代码

```python
n = input()
k = int(input())

stack = []
for i in n:
    while stack and i < stack[-1] and k > 0:
        stack.pop()
        k -= 1
    stack.append(i)

if k > 0:
    print(int(''.join(stack[:-k])))
else:
    print(int(''.join(stack)))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![局部截取_20251209_191929](D:\to@ GitHub\启动\LittleBeetroot1666\启动\2025fallCS101--------\Project\assignments\assignmentD\z_appendix\局部截取_20251209_191929.png)

![局部截取_20251209_191938](D:\to@ GitHub\启动\LittleBeetroot1666\启动\2025fallCS101--------\Project\assignments\assignmentD\z_appendix\局部截取_20251209_191938.png)



### E30091:缺德的图书馆管理员

greedy, http://cs101.openjudge.cn/practice/30091

耗时：5min

思路：题干描述的类似高中时候做过的数学题“士兵过桥”问题，属于经典数学题的第一问难度，用所有人分别与走廊两端的距离的最大值和最小值取代时间的最大值和最小值即可。



代码

```python
l = int(input())
n = int(input())
js = list(map(int, input().split()))
ks = []
for j in js:
    if j <= l // 2:
        ks.append(j)
    else:
        ks.append(l + 1 - j)
print(max(ks), l + 1 - min(ks))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![局部截取_20251209_012949](D:\to@ GitHub\启动\LittleBeetroot1666\启动\2025fallCS101--------\Project\assignments\assignmentD\z_appendix\局部截取_20251209_012949.png)

![局部截取_20251209_013018](D:\to@ GitHub\启动\LittleBeetroot1666\启动\2025fallCS101--------\Project\assignments\assignmentD\z_appendix\局部截取_20251209_013018.png)



### M27371:Playfair密码

simulation，string，matrix,  implemention http://cs101.openjudge.cn/practice/27371

耗时：4h

思路：自己用了矩阵和哈希表进行处理，结果样例都能过，却一直WA。

后来就自己打了一遍上课题解的代码，学会了诸如replace()函数和pos_map()函数的用法。



代码

能AC的代码：

```python
import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    key_input = input_data[0]
    n = int(input_data[1])
    plaintexts = input_data[2:]

    # 使用replace函数把'j'全部转换为'i'
    key = key_input.lower().replace('j', 'i')
    alpha = 'abcdefghiklmnopqrstuvwxyz'
    matrix_chars = []
    seen = set()

    for char in key:
        if char not in seen:
            seen.add(char)
            matrix_chars.append(char)

    for char in alpha:
        if char not in seen:
            seen.add(char)
            matrix_chars.append(char)

    matrix = [matrix_chars[i: i + 5] for i in range(0, 25, 5)]
    pos_map = {char: (i // 5, i % 5) for i, char in enumerate(matrix_chars)}

    def encrypt_text(text):
        # 使用replace函数把'j'全部转换为'i'
        text = text.lower().replace('j', 'i')
        res = []
        i = 0
        length = len(text)

        while i < length:
            a = text[i]
            b = ''

            if i + 1 < length:
                b = text[i + 1]

                if a == b:
                    b = 'q' if a == 'x' else 'x'
                    i += 1
                else:
                    i += 2
            else:
                b = 'q' if a == 'x' else 'x'
                i += 1

            # 使用pos_map获取行数和列数
            r1, c1 = pos_map[a]
            r2, c2 = pos_map[b]
            if r1 == r2:
                res.append(matrix[r1][(c1 + 1) % 5])
                res.append(matrix[r2][(c2 + 1) % 5])
            elif c1 == c2:
                res.append(matrix[(r1 + 1) % 5][c1])
                res.append(matrix[(r2 + 1) % 5][c2])
            else:
                res.append(matrix[r1][c2])
                res.append(matrix[r2][c1])

        return ''.join(res)

    for text in plaintexts:
        print(encrypt_text(text))


if __name__ == '__main__':
    solve()

```

自己写的代码：

```python
def k0j(listy):
    return ''.join(listy)


key = input()

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
kg = []
sl = {}
itt = 0
ress = []
for ki in key:
    if ki == 'j' and 'i' not in sl:
        sl['i'] = [itt // 5, itt % 5]
        kg.append('i')
        itt += 1
    elif ki not in sl:
        sl[ki] = [itt // 5, itt % 5]
        kg.append(ki)
        itt += 1
for ai in alpha:
    if ai not in sl:
        sl[ai] = [itt // 5, itt % 5]
        kg.append(ai)
        itt += 1

for _ in range(int(input())):
    tara = input()
    res = []
    tof = len(tara)
    itig = 0
    while itig < tof - 1:
        if tara[itig] != tara[itig + 1]:
            a = tara[itig]
            b = tara[itig + 1]
            itig += 2
        else:
            if tara[itig] == 'x':
                a = tara[itig]
                b = 'q'
                itig += 1
            else:
                a = tara[itig]
                b = 'x'
                itig += 1

        if a == 'j':
            a = 'i'
        if b == 'j':
            b = 'i'

        if sl[a][0] == sl[b][0]:
            res.append(kg[(sl[a][0] * 5 + (sl[a][1] + 1) % 5) % 25])
            res.append(kg[(sl[b][0] * 5 + (sl[b][1] + 1) % 5) % 25])
        elif sl[a][1] == sl[b][1]:
            res.append(kg[((sl[a][0] + 1) % 5 * 5 + sl[a][1]) % 25])
            res.append(kg[((sl[b][0] + 1) % 5 * 5 + sl[b][1]) % 25])
        else:
            res.append(kg[(sl[a][0] * 5 + sl[b][1]) % 25])
            res.append(kg[(sl[b][0] * 5 + sl[a][1]) % 25])

    if itig == tof - 1:
        a = tara[itig]
        if a == 'x':
            b = 'q'
        else:
            b = 'x'
        
        if sl[a][0] == sl[b][0]:
            res.append(kg[(sl[a][0] * 5 + (sl[a][1] + 1) % 5) % 25])
            res.append(kg[(sl[b][0] * 5 + (sl[b][1] + 1) % 5) % 25])
        elif sl[a][1] == sl[b][1]:
            res.append(kg[((sl[a][0] + 1) % 5 * 5 + sl[a][1]) % 25])
            res.append(kg[((sl[b][0] + 1) % 5 * 5 + sl[b][1]) % 25])
        else:
            res.append(kg[(sl[a][0] * 5 + sl[b][1]) % 25])
            res.append(kg[(sl[b][0] * 5 + sl[a][1]) % 25])

    ress.append(k0j(res))

for res in ress:
    print(res)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![局部截取_20251209_202300](D:\to@ GitHub\启动\LittleBeetroot1666\启动\2025fallCS101--------\Project\assignments\assignmentD\z_appendix\局部截取_20251209_202300.png)

![局部截取_20251209_202314](D:\to@ GitHub\启动\LittleBeetroot1666\启动\2025fallCS101--------\Project\assignments\assignmentD\z_appendix\局部截取_20251209_202314.png)

![局部截取_20251209_202822](D:\to@ GitHub\启动\LittleBeetroot1666\启动\2025fallCS101--------\Project\assignments\assignmentD\z_appendix\局部截取_20251209_202822.png)

![局部截取_20251209_202903](D:\to@ GitHub\启动\LittleBeetroot1666\启动\2025fallCS101--------\Project\assignments\assignmentD\z_appendix\局部截取_20251209_202903.png)



### T30201:旅行售货商问题

dp,dfs, http://cs101.openjudge.cn/practice/30201

耗时：2h

思路：暴力枚举不是TLE就是MLE

AI提供的思路，使用了状态压缩dp，要求我们对二进制和位运算能够灵活掌握，有难度，但是代码将时间复杂度和空间复杂度由O(n!)减小至O(n * 2 ** n)，在OpenJudge的Pypy3环境运行能AC。



代码

```python
n = int(input())
res = float('inf')
matrix = [list(map(int, input().split())) for _ in range(n)]

dp = [[float('inf')] * n for _ in range(1 << n)]
dp[1 << 0][0] = 0

for mask in range(1 << n):
    for u in range(n):
        if not (mask & (1 << u)):
            continue
        for v in range(n):
            if mask & (1 << v):
                continue
            new_mask = mask | (1 << v)

            if dp[new_mask][v] > dp[mask][u] + matrix[u][v]:
                dp[new_mask][v] = dp[mask][u] + matrix[u][v]

full_mask = (1 << n) - 1
for u in range(n):
    res = min(res, dp[full_mask][u] + matrix[u][0])

print(res)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>![局部截取_20251209_192527](D:\to@ GitHub\启动\LittleBeetroot1666\启动\2025fallCS101--------\Project\assignments\assignmentD\z_appendix\局部截取_20251209_192527.png)

![局部截取_20251209_192535](D:\to@ GitHub\启动\LittleBeetroot1666\启动\2025fallCS101--------\Project\assignments\assignmentD\z_appendix\局部截取_20251209_192535.png)



### T30204:小P的LLM推理加速

greedy, http://cs101.openjudge.cn/practice/30204

https://www.luogu.com.cn/problem/P14635

耗时：2h

思路：常规贪心，先尽可能购买“便宜”的第一块糖果（价格不大于最便宜的一组糖果的总价的一半），再用剩下的钱全部购买最便宜的一组糖果即可。

OpenJudge上AC不成问题，洛谷上数据只能部分通过，洛谷官方题解全部是C和C++语言，我也无法知道洛谷上没有通过的题例是什么样的数据。



代码

```python
n, m = list(map(int, input().split()))
min_circ = float('inf')
birds = []
asq = []
for _ in range(n):
    i, j = list(map(int, input().split()))
    birds.append(i)
    if i + j < min_circ:
        min_circ = i + j
        asq.append(max(i, j))

early_birds = []
late_birds = [asq[-1]]
for i in birds:
    if i <= min_circ // 2:
        early_birds.append(i)
    elif min_circ // 2 < i <= asq[-1]:
        late_birds.append(i)
early_birds.sort()
late_birds.sort()

cnt = 0
sgm = 0
s0 = sum(early_birds)
l0 = len(early_birds)
if m == s0:
    print(l0)
elif m < s0:
    init_eb = 0
    while sgm <= m - early_birds[init_eb]:
        sgm += early_birds[init_eb]
        init_eb += 1
    print(init_eb)
else:
    m -= s0
    cnt += l0
    cnt += 2 * m // min_circ
    m = m % min_circ
    print(cnt)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![局部截取_20251209_191450](D:\to@ GitHub\启动\LittleBeetroot1666\启动\2025fallCS101--------\Project\assignments\assignmentD\z_appendix\局部截取_20251209_191450.png)

![局部截取_20251209_191559](D:\to@ GitHub\启动\LittleBeetroot1666\启动\2025fallCS101--------\Project\assignments\assignmentD\z_appendix\局部截取_20251209_191559.png)

![局部截取_20251209_191518](D:\to@ GitHub\启动\LittleBeetroot1666\启动\2025fallCS101--------\Project\assignments\assignmentD\z_appendix\局部截取_20251209_191518.png)

![局部截取_20251209_191644](D:\to@ GitHub\启动\LittleBeetroot1666\启动\2025fallCS101--------\Project\assignments\assignmentD\z_appendix\局部截取_20251209_191644.png)

![局部截取_20251209_191841](D:\to@ GitHub\启动\LittleBeetroot1666\启动\2025fallCS101--------\Project\assignments\assignmentD\z_appendix\局部截取_20251209_191841.png)

![局部截取_20251209_191759](D:\to@ GitHub\启动\LittleBeetroot1666\启动\2025fallCS101--------\Project\assignments\assignmentD\z_appendix\局部截取_20251209_191759.png)



## 2. 学习总结和收获

通过这次月考，我更加深刻地认识到自己的不足：我对于栈、队列等数据类型掌握地不够熟练(E29946)，不了解状态压缩算法(T30201)，对二进制和位运算不能灵活使用(T30201)，哈希表和矩阵综合应用会犯糊涂(M27371)，不能短时间内灵活处理较难的贪心问题(T30204)。

接下来的几周还需要在这些方面多多加强。

如果作业题目简单，有否额外练习题目，比如：OJ“计概2025fall每日选做”、CF、LeetCode、洛谷等网站题目。

这周较忙，仅在CodeForces上参加周赛并少量刷题。

![局部截取_20251209_190830](D:\to@ GitHub\启动\LittleBeetroot1666\启动\2025fallCS101--------\Project\assignments\assignmentD\z_appendix\局部截取_20251209_190830.png)
