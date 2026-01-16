# Assignment #7: 矩阵、队列、贪心

Updated 1315 GMT+8 Oct 21, 2025

2025 fall, Complied by <mark>郭旭杰、化学与分子工程学院</mark>

OpenJudge账号：25n2500011906，昵称：郭旭杰

CodeForces账号：LittleBeetroot，段位：Newbie（新手）



>**说明：**
>
>1. **解题与记录：**
>
>  对于每一个题目，请提供其解题思路（可选），并附上使用Python或C++编写的源代码（确保已在OpenJudge， Codeforces，LeetCode等平台上获得Accepted）。请将这些信息连同显示“Accepted”的截图一起填写到下方的作业模板中。（推荐使用Typora https://typoraio.cn 进行编辑，当然你也可以选择Word。）无论题目是否已通过，请标明每个题目大致花费的时间。
>
>2. 提交安排：**提交时，请首先上传PDF格式的文件，并将.md或.doc格式的文件作为附件上传至右侧的“作业评论”区。确保你的Canvas账户有一个清晰可见的本人头像，提交的文件为PDF格式，并且“作业评论”区包含上传的.md或.doc附件。
> 
>4. **延迟提交：**如果你预计无法在截止日期前提交作业，请提前告知具体原因。这有助于我们了解情况并可能为你提供适当的延期或其他帮助。  
>
>请按照上述指导认真准备和提交作业，以保证顺利完成课程要求。





## 1. 题目

### M12560: 生存游戏

matrices, http://cs101.openjudge.cn/pctbook/M12560/

耗时：15min速通，没什么难度。

思路：就是要在矩阵外围加一层保护圈，输出前再去掉。

![局部截取_20251026_220356](D:\腾讯电脑管家截图文件\局部截取_20251026_220356.png)

代码

```python
n, m = list(map(int, input().split()))
matrix = []
row0 = [0 for i in range(m + 2)]
matrix.append(row0)
for i in range(1, n + 1):
    row = list(map(int, input().split()))
    row1 = [0]
    for j in range(m):
        row1.append(row[j])
    row1.append(0)
    matrix.append(row1)
matrix.append(row0)

new_matrix = []
for i in range(1, n + 1):
    new_row = []
    for j in range(1, m + 1):
        new_row.append(matrix[i][j])
    new_matrix.append(new_row)

for i in range(1, n + 1):
    for j in range(1, m + 1):
        sgm = matrix[i - 1][j - 1] + matrix[i - 1][j] + matrix[i - 1][j + 1] + matrix[i][j - 1] + matrix[i][j + 1] + matrix[i + 1][j - 1] + matrix[i + 1][j] + matrix[i + 1][j + 1]
        if matrix[i][j] == 1:
            if 2 <= sgm <= 3:
                new_matrix[i - 1][j - 1] = 1
            else:
                new_matrix[i - 1][j - 1] = 0
        if matrix[i][j] == 0:
            if sgm == 3:
                new_matrix[i - 1][j - 1] = 1
            else:
                new_matrix[i - 1][j - 1] = 0



for new_row in new_matrix:
    print(*new_row)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](D:\腾讯电脑管家截图文件\局部截取_20251026_220333.png)



### M04133:垃圾炸弹

matrices, http://cs101.openjudge.cn/pctbook/M04133/

耗时：找思路找了两天，找到思路后20min速通。

思路：与雷达安装问题相似，涉及变换参考系，可以以垃圾为参考系，在其周围一定半径内安装炸弹所能产生的有效值相应增加。找到有效值最大的点即可。

涉及到max(),min()函数的巧妙运用。

代码

```python
d = int(input())
n = int(input())
matrix = [[0 for i in range(1025)] for j in range(2025)]
js = []
for _ in range(n):
    x, y, h = list(map(int, input().split()))
    for i in range(max(x - d, 0), min(x + d + 1, 1025)):
        for j in range(max(y - d, 0), min(y + d + 1, 1025)):
            matrix[i][j] += h
for i in range(1025):
    for j in range(1025):
        js.append(matrix[i][j])
js.sort(reverse=True)
cnt = 0
while js[cnt] == js[0]:
    cnt += 1
print(cnt, js[0])

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![局部截取_20251026_220616](D:\腾讯电脑管家截图文件\局部截取_20251026_220616.png)

![局部截取_20251026_221017](D:\腾讯电脑管家截图文件\局部截取_20251026_221017.png)



### M02746: 约瑟夫问题

implementation, queue, http://cs101.openjudge.cn/pctbook/M02746/

耗时：25分钟通过，有一点难度。

思路：让列表环化有点难度，还有就是在不断淘汰猴子的过程中，猴子的总数发生变化，这也会使列表的长度减小。

代码

```python
blacklist = 0
while blacklist == 0:
    n, m = list(map(int, input().split()))
    if m + n >= 1:
        otto = []
        cnt = 0
        o = 0
        for i in range(1, n + 1):
            otto.append(i)
        while len(otto) > 1:
            cnt += 1
            o += 1
            if cnt == m:
                cnt = 0
                ot = (o - 1) % len(otto)
                otto.remove(otto[ot])
                o = ot
        print(*otto)
    else:
        blacklist = 1
        break

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![局部截取_20251026_221227](D:\腾讯电脑管家截图文件\局部截取_20251026_221227.png)

![局部截取_20251026_221245](D:\腾讯电脑管家截图文件\局部截取_20251026_221245.png)



### M26976:摆动序列

greedy, http://cs101.openjudge.cn/pctbook/M26976/


思路：30min通过，思路好找，但有点难。

转化列表，先排除相等情况，再逐对排查，有动态规划思想。

代码

```python
n = int(input())
js = list(map(int, input().split()))

if n == 1 or max(js) - min(js) == 0:
    print(1)
elif n == 2 and js[0]!=js[1]:
    print(2)
else:
    k = 0

    stt = 1
    v = 0
    ks = [js[i] - js[i - 1] for i in range(1, n)]
    if 0 in ks:
        ks.remove(0)
    if ks[0] < 0:
        stt = -1

    for i in range(0, len(ks)):
        if ks[i] // stt > 0:
            stt *= (-1)
            k += 1

    print(k + 1)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![局部截取_20251026_221620](D:\腾讯电脑管家截图文件\局部截取_20251026_221620.png)

![局部截取_20251026_221929](D:\腾讯电脑管家截图文件\局部截取_20251026_221929.png)



### T26971:分发糖果

greedy, http://cs101.openjudge.cn/pctbook/T26971/

耗时：5天（找了3天思路后发现思路还是错的，后来看了LeetCode上面的原题题解才恍然大悟）。

思路：需要注意，如果两个小孩评分相等，那么这两个小孩得到的糖无论谁多谁少，差距多大，在规则上都是合理的，所以相对于定义的mounti函数，更适用于hillgravedown函数。

定义之后直接调用函数即可。

注意贪心算法使用时也不要理所当然地认为相邻两个小孩的糖个数相差1就是最优解。

代码

```python
def hillgravedown(listy):
    hillgravedown_n = len(listy)
    hilldown_left = [0] * hillgravedown_n
    for i in range(hillgravedown_n):
        if i > 0 and listy[i] > listy[i - 1]:
            hilldown_left[i] = hilldown_left[i - 1] + 1
        else:
            hilldown_left[i] = 1

    hilldown_right = hillgravedown_dust = 0
    for i in range(hillgravedown_n - 1, -1, -1):
        if i < hillgravedown_n - 1 and listy[i] > listy[i + 1]:
            hilldown_right += 1
        else:
            hilldown_right = 1
        hillgravedown_dust += max(hilldown_left[i], hilldown_right)

    return hillgravedown_dust


n = int(input())
js = list(map(int, input().split()))
print(hillgravedown(js))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![局部截取_20251026_230720](D:\腾讯电脑管家截图文件\局部截取_20251026_230720.png)

![局部截取_20251026_230728](D:\腾讯电脑管家截图文件\局部截取_20251026_230728.png)



### 1868A. Fill in the Matrix

constructive algorithms, implementation, 1300, https://codeforces.com/problemset/problem/1868/A

耗时：5天（找了一天思路，代码调整了4天）。

思路：只要让数字从小往大逐个排列，然后不断把第一个数放到队列末尾，直到达到n或者只剩一种情况，如果没有达到n就一直填原始序列genlistie直到n行为止。

代码

```python
def to_listie(n_to_listie):
    return [i_to_listie for i_to_listie in range(n_to_listie)]


def str_to_listie(n_to_listie):
    return [str(i_to_listie) for i_to_listie in range(n_to_listie)]


def cata_findm(n0, m0):
    if m0 == 1:
        return 0
    else:
        return min(n0 + 1, m0)


def alter_listie(listy):
    first = listy.pop(0)
    listy.append(first)
    return listy


def kpj(strry_listy):
    return ' '.join(strry_listy)


Lne = int(input())
for _l in range(Lne):
    n, m = list(map(int, input().split()))
    print(cata_findm(n, m))
    if m == 1:
        for _ in range(n):
            print(0)
    else:
        genlistie = str_to_listie(m)
        ltt = str_to_listie(m)
        cnt = 1
        while cnt <= min(m - 1, n):
            print(kpj(ltt))
            cnt += 1
            ltt = alter_listie(ltt)
        if m - 1 < n:
            for _ in range(n - m + 1):
                print(kpj(genlistie))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![局部截取_20251026_230926](D:\腾讯电脑管家截图文件\局部截取_20251026_230926.png)

![局部截取_20251026_230914](D:\腾讯电脑管家截图文件\局部截取_20251026_230914.png)



## 2. 学习总结和收获

学习了矩阵相关问题（M12560: 生存游戏、M04133:垃圾炸弹、1868A. Fill in the Matrix）和序列贪心（M02746: 约瑟夫问题、M26976:摆动序列、T26971:分发糖果）问题

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2025fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

做了约瑟夫问题的升级版：

## M03254:约瑟夫问题No.2

implantation，[OpenJudge - M03254:约瑟夫问题No.2](http://cs101.openjudge.cn/pctbook/M03254/)

耗时：15分钟速通。

思路：与约瑟夫问题差不多。

代码

```python
blacklist = 0
while blacklist == 0:
    n, p, m = list(map(int, input().split()))
    if m + n + p >= 1:
        otto = []
        cnt = 0
        o = p - 1
        shuodedaoli = []
        for i in range(1, n + 1):
            otto.append(i)
        while len(otto) > 1:
            cnt += 1
            o += 1
            if cnt == m:
                cnt = 0
                ot = (o - 1) % len(otto)
                shuodedaoli.append(otto[ot])
                otto.remove(otto[ot])
                o = ot
        shuodedaoli.append(otto[0])
        print(','.join(map(str, shuodedaoli)))
    else:
        blacklist = 1
        break

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![局部截取_20251026_224844](D:\腾讯电脑管家截图文件\局部截取_20251026_224844.png)

![局部截取_20251026_224853](D:\腾讯电脑管家截图文件\局部截取_20251026_224853.png)



又做了一些简单题练手。

自学了def函数的用法以及面向对象的编程方法（LeetCode上面几乎每一题前两行都是class和def）

为解决问题引入的定义：

```python
def to_listie(n_to_listie):
    return [i_to_listie for i_to_listie in range(n_to_listie)]


def str_to_listie(n_to_listie):
    return [str(i_to_listie) for i_to_listie in range(n_to_listie)]


def to_str(listy):
    return[str(i_in_listy) for i_in_listy in listy]
    
    
def cata_findm(n0, m0):
    if m0 == 1:
        return 0
    else:
        return min(n0 + 1, m0)


def alter_listie(listy):
    first = listy.pop(0)
    listy.append(first)
    return listy


def kpj(strry_listy):
    return ' '.join(strry_listy)


def mounti(listie):
    mount_altitude = [0]
    for i in range(1, len(listie)):
        if listie[i] > listie[i - 1]:
            mount_altitude.append(mount_altitude[-1] + 1)
        elif listie[i] < listie[i - 1]:
            mount_altitude.append(mount_altitude[-1] - 1)
        else:
            mount_altitude.append(mount_altitude[-1])
    base_altitude = min(mount_altitude) - 1
    mount_waterfill = -len(listie) * base_altitude
    mount_seasum = sum(mount_altitude)
    mount_landsum = mount_seasum + mount_waterfill
    return mount_landsum


def hillgravedown(listy):
    hillgravedown_n = len(listy)
    hilldown_left = [0] * hillgravedown_n
    for i in range(hillgravedown_n):
        if i > 0 and listy[i] > listy[i - 1]:
            hilldown_left[i] = hilldown_left[i - 1] + 1
        else:
            hilldown_left[i] = 1

    hilldown_right = hillgravedown_dust = 0
    for i in range(hillgravedown_n - 1, -1, -1):
        if i < hillgravedown_n - 1 and listy[i] > listy[i + 1]:
            hilldown_right += 1
        else:
            hilldown_right = 1
        hillgravedown_dust += max(hilldown_left[i], hilldown_right)

    return hillgravedown_dust

```

有的函数可以简化输入（如kpj可以将列表转化为带空格的一串数字输出，常用且好用）

有的可以简化逻辑，避免模块需要逐个排查的问题（mounti就在某些题目中有类似用法）

还有的因题而异（cata_findm就是针对特定的题目而非题目类型定义的）

一般函数名越长，意味着使用得可能越少（如mounti的使用频率要显著高于hillgravedown）

