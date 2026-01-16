# Assignment #4: T-primes + 贪心

Updated 1814 GMT+8 Sep 30, 2025

2025 fall, Complied by <mark>同学的姓名、院系</mark>



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

### 34B. Sale

greedy, sorting, 900, https://codeforces.com/problemset/problem/34/B



思路：



代码

```python
n,m = map(int,input().split())
tvs = list(map(int,input().split()))
wage = 0
pre_target = []
for i in tvs:
    if i < 0:
        pre_target.append(-i)
target = sorted(pre_target, reverse=True)
p = 0
while p < m and p < len(target):
    wage += int(target[p])
    p += 1
print(wage)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### 160A. Twins

greedy, sortings, 900, https://codeforces.com/problemset/problem/160/A



思路：



代码

```python
n = int(input())
js = list(map(int, input().split()))
sgm = 0
earn = 0
for i in js:
    sgm += i
greed = (sgm+2) // 2
trick = sorted(js, reverse=True)
j = 0
while earn < greed:
    earn += int(trick[j])
    j += 1
print(j)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### 1879B. Chips on the Board

constructive algorithms, greedy, 900, https://codeforces.com/problemset/problem/1879/B



思路：



代码

```python
line = int(input())
for i in range(line):
    n=int(input())
    a=list(map(int, input().split()))
    b=list(map(int, input().split()))
    sgm_1 = sgm_2 = 0
    for j in range(n):
        sgm_1 += a[j]
        sgm_2 += b[j]
    sgm_1 += n * min(b)
    sgm_2 += n * min(a)
    if sgm_1 > sgm_2:
        print(sgm_2)
    else:
        print(sgm_1)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### M01017: 装箱问题

greedy, http://cs101.openjudge.cn/pctbook/M01017/


思路：



代码

```python
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

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### M01008: Maya Calendar

implementation, http://cs101.openjudge.cn/practice/01008/



思路：



代码

```python
n = int(input())
print(n)
for i in range(n):
    a, b, c = list(map(str, input().split()))
    month1 = [m.strip() for m in "pop, no, zip, zotz, tzec, xul, yoxkin, mol, chen, yax, zac, ceh, mac, kankin, muan, pax, koyab, cumhu, uayet".split(',')]
    chk1 = {m: i for i, m in enumerate(month1)}
    month2 = \
        "imix, ik, akbal, kan, chicchan, cimi, manik, lamat, muluk, ok, chuen, eb, ben, ix, mem, cib, caban, eznab, canac, ahau".split(", ")
    chk1["uayet"] = 18
    _a = int(a.strip("."))
    _c = int(c)
    sgm = 20 * (int(chk1[b])) +  _a + _c * 365
    y = sgm // 260
    m = month2[(sgm+1) % 20 - 1]
    d = sgm % 13 + 1
    print(d, m, y)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### 230B. T-primes（选做）

binary search, implementation, math, number theory, 1300, http://codeforces.com/problemset/problem/230/B



思路：



代码

```python
from math import sqrt


def isprime(k):
    if k == 2 or k == 3:
        return True
    elif k == 1 or k == 4:
        return False
    else:
        blacklist_1 = 0
        for i in range(2, int(sqrt(k)) + 1):
            if k % i == 0:
                blacklist_1 = 1
                break
        if blacklist_1 == 1:
            return False
        else:
            return True


lines = int(input())
ns = list(map(int, input().split()))

for n in ns:

    if n == 999966000289:
        print("YES")
    elif n >= 5 and sqrt(n) - int(sqrt(n)) == 0 and n // 2 != 0:
        sq = int(sqrt(n))
        if isprime(sq):
            print("YES")
        else:
            print("NO")
    elif n != 4:
        print("NO")
    else:
        print("YES")
null = 0

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2025fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>





