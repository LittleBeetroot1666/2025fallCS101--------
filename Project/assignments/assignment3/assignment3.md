# Assignment #3: 语法练习

Updated 1440 GMT+8 Sep 23, 2025

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

### E28674:《黑神话：悟空》之加密

http://cs101.openjudge.cn/pctbook/E28674/



思路：



代码

```python
k = int(input())
ki = k % 26
L = []
nums = []
Lplus = []
st = input()
string = list(st)
for s in string:
    L.append(s)
for i in L:
    if 64 <= ord(i) <= 90:
        t = ord(i)-ki
        if t <= 64:
            t += 26
        ts = chr(t)
        Lplus.append(ts)
    elif 97 <= ord(i) <= 123:
        t = ord(i) - ki
        if t < 97:
            t += 26
        ts = chr(t)
        Lplus.append(ts)
result = "".join(Lplus)
print(result)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### E28691: 字符串中的整数求和

http://cs101.openjudge.cn/pctbook/E28691/



思路：



代码

```python
ipt = input().strip()
js = []
for i in ipt:
    if i.isdigit():
        js.append(int(i))
sgm = 10 * js[0] + js[1] + 10 * js[2] + js[3]
print(sgm)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### M28664: 验证身份证号 

http://cs101.openjudge.cn/pctbook/M28664/



思路：



代码

```python
line = int(input())
for i in range(line):
    c0 = input()
    c=list(c0)
    t = []
    for cs in c:
        if cs.isdigit():
            t.append(int(cs))
        else:
            t.append(10)
    ds = t[0]*7+t[1]*9+t[2]*10+t[3]*5+t[4]*8+t[5]*4+t[6]*2+t[7]*1+t[8]*6+t[9]*3+t[10]*7+t[11]*9+t[12]*10+t[13]*5+t[14]*8+t[15]*4+t[16]*2
    ktry = ds%11
    if ktry+t[-1] == 1 or ktry+t[-1] ==12:
        print("YES")
    else:
        print("NO")

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### M28678: 角谷猜想

http://cs101.openjudge.cn/pctbook/M28678/


思路：



代码

```python
n = int(input())
while n >= 2:
    if n % 2 == 1:
        print(f"{n}*3+1={n*3+1}")
        n = n * 3 + 1
    else:
        print(f"{n}/2={n//2}")
        n = n // 2 
print("End")

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### M28700: 罗马数字与整数的转换

http://cs101.openjudge.cn/pctbook/M28700/



思路：



代码

```python
ipt = input()
r = []
for i in range(1, 4000):
    ip = i
    null = 0
    if ip < 4000:
        i = int(ip)
        Rom = []
        t = i // 1000
        h = i % 1000 // 100
        m = i % 100 // 10
        s = i % 10
        if t == 3:
            Rom.append("MMM")
        elif t == 2:
            Rom.append("MM")
        elif t == 1:
            Rom.append("M")
        else:
            null = 0
        if h == 9:
            Rom.append("CM")
        elif h == 8:
            Rom.append("DCCC")
        elif h == 7:
            Rom.append("DCC")
        elif h == 6:
            Rom.append("DC")
        elif h == 5:
            Rom.append("D")
        elif h == 4:
            Rom.append("CD")
        elif h == 3:
            Rom.append("CCC")
        elif h == 2:
            Rom.append("CC")
        elif h == 1:
            Rom.append("C")
        else:
            null = 0
        if m == 9:
            Rom.append("XC")
        elif m == 8:
            Rom.append("LXXX")
        elif m == 7:
            Rom.append("LXX")
        elif m == 6:
            Rom.append("LX")
        elif m == 5:
            Rom.append("L")
        elif m == 4:
            Rom.append("XL")
        elif m == 3:
            Rom.append("XXX")
        elif m == 2:
            Rom.append("XX")
        elif m == 1:
            Rom.append("X")
        else:
            null = 0
        if s == 9:
            Rom.append("IX")
        elif s == 8:
            Rom.append("VIII")
        elif s == 7:
            Rom.append("VII")
        elif s == 6:
            Rom.append("VI")
        elif s == 5:
            Rom.append("V")
        elif s == 4:
            Rom.append("IV")
        elif s == 3:
            Rom.append("III")
        elif s == 2:
            Rom.append("II")
        elif s == 1:
            Rom.append("I")
        else:
            null = 0
        rom = "".join(map(str, Rom))
        r.append(rom)
    else:
        null = 0
if ipt.isdigit():
    d = int(ipt)-1
    print(r[d])
else:
    j = 0
    while r[j] != ipt:
        j = j + 1
    print(j + 1)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### 158B. Taxi

*special problem, greedy, implementation, 1100,  https://codeforces.com/problemset/problem/158/B



思路：



代码

```python
n = int(input())
js = list(map(int, input().split()))
s = []
s1 = 0
s2 = 0
s3 = 0
s4 = 0
t = 0
for j in js:
    s.append(j)
for i in s:
    if i == 4:
        s4 += 1
    elif i == 3:
        s3 += 1
    elif i == 2:
        s2 += 1
    else:
        s1 += 1
t += s4
t += s3
s1 -= s3
if s2 % 2 == 0:
    t += s2 // 2
else:
    t += s2 // 2
    t += 1
    s1 -= 2
if s1 <= 0:
    t += 0
else:
    t += (s1 + 3) // 4
print(t)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2025fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>





