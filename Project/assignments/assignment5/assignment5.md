# Assignment #5: 20251009 cs101 Mock Exam寒露第二天

Updated 1651 GMT+8 Oct 9, 2025

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

### E29895: 分解因数

implementation, http://cs101.openjudge.cn/practice/29895/



思路：



代码

```python
n = int(input())
i = 2
while n % i != 0:
    i += 1
print(n // i)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### E29940: 机器猫斗恶龙

greedy, http://cs101.openjudge.cn/practice/29940/



思路：



代码

```python
n = int(input())
js = list(map(int,input().split()))
sgm = 0
s = []
for j in js:
    sgm += j
    s.append(sgm)
m = min(s)
if m < 0:
    res = 1-m
else:
    res = 1
print(res)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### M29917: 牛顿迭代法

implementation, http://cs101.openjudge.cn/practice/29917/



思路：



代码

```python
while True:
    try:
        t = float(input())
        x = 1
        y = 1 - t
        k = 0
        while abs(y/(2*x)) > 1e-6:
            x -= y / (2*x)
            y = x**2 - t
            k += 1
        x -= y / (2*x)
        k += 1
        print(k,"%.2f" % x)
    except:
        break

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### M29949: 贪婪的哥布林

greedy, http://cs101.openjudge.cn/practice/29949/


思路：



代码

```python
n,m = map(int, input().split())
js = []
sgm = 0
earn = 0
for _ in range(n):
    v,w = map(int, input().split())
    js.append((v / w,v,w))
js.sort(reverse=True)
for j in js:
    if sgm + j[2] <= m:
        sgm += j[2]
        earn += j[1]
    else:
        earn += j[0] * (m - sgm)
        sgm = m
        break
print("%.2f" % earn)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### M29918: 求亲和数

implementation, http://cs101.openjudge.cn/practice/29918/



思路：



代码

```python
# Time Limit Exceeded
t = int(input())
n = [0]
for i in range(2,100001):
    d = 0
    for j in range(1,int(i**0.5)+1):
        if i % j == 0:
            if j ** 2 == i or j == 1:
                d += j
            else:
                d += j + i // j
    n.append(d)
for i in range(2,100001):
    if n[i-1] > 99999:
        continue
    elif n[n[i-1]-1]== i:
        if i < n[i-1] <= t:
            print(i,n[i-1])

```



```python
n = int(input())
if n >= 284:
    print(220,284)
if n >= 1210:
    print(1184,1210)
if n >= 2924:
    print(2620,2924)
if n >= 5564:
    print(5020,5564)
if n >= 6368:
    print(6232,6368)
if n >= 10856:
    print(10744,10856)
if n >= 14595:
    print(12285,14595)
if n >= 18416:
    print(17296,18416)
if n >= 76084:
    print(63020,76084)
if n >= 66992:
    print(66928,66992)
if n >= 71145:
    print(67095,71145)
if n >= 87633:
    print(69615,87633)
if n >= 88730:
    print(79750,88730)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### T29947:校门外的树又来了（选做）

http://cs101.openjudge.cn/practice/29947/



思路：



代码

```python
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

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2025fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>





