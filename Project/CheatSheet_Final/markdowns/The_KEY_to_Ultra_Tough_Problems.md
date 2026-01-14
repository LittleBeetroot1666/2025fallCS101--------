## The_KEY_to_Ultra_Tough_Problems

### 1.Tricky_Problems

![局部截取_20251224_195548](D:\腾讯电脑管家截图文件\局部截取_20251224_195548.png)

```python
# 25353: 排队
# 题意：每次只能交换相邻且身高差不超过 D 的人，求字典序最小的最终排列
# 思路：将允许交换关系看作有向无环图（DAG），每次取“入度为 0”的人中身高最小者输出。
# 实现：多轮扫描——每轮找出当前所有入度为 0 的节点集合 S，
#       对 S 内按身高升序输出并从序列中删除，重复直到序列为空。
# 注意：最坏情况下复杂度为 O(N^2)。

import sys
input = sys.stdin.readline

def solve():
    line = input().split()
    if not line:
        return
    n, D = map(int, line)
    arr = [int(input()) for _ in range(n)]

    result = []
    cur = arr[:]  # 当前剩余队列

    while cur:
        m = len(cur)
        S_idx = []  # 当前入度为 0 的位置下标
        left_min = None
        left_max = None

        for i in range(m):
            h = cur[i]
            if i == 0:
                # 第一个人必然没有左侧约束，入度为 0
                S_idx.append(i)
                left_min = h
                left_max = h
                continue

            # 判断是否满足：与左侧所有人身高差均 ≤ D
            # 即 h 必须位于 [left_max - D, left_min + D] 区间内
            if left_max - D <= h <= left_min + D:
                S_idx.append(i)

            # 更新左侧区间最小/最大值
            if h < left_min:
                left_min = h
            if h > left_max:
                left_max = h

        # 收集并按身高升序排序
        S = [cur[i] for i in S_idx]
        S.sort()

        # 输出这些人
        result.extend(S)

        # 删除已输出的元素（保持原相对顺序）
        to_remove = set(S_idx)
        cur = [cur[i] for i in range(m) if i not in to_remove]

    # 输出结果
    print('\n'.join(map(str, result)))


if __name__ == "__main__":
    solve()
```



![局部截取_20251224_195717](D:\腾讯电脑管家截图文件\局部截取_20251224_195717.png)

```python
def hillgravedown(listy):
    hillgravedown_n = len(listy)
    hilldown_left = [0] * hillgravedown_n
    for i in range(hillgravedown_n):
        if i > 0 and listy[i] > listy[i - 1]:
            hilldown_left[i] = hilldown_left[i-1] + 1
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



![局部截取_20251224_203149](D:\腾讯电脑管家截图文件\局部截取_20251224_203149.png)

```python
def mov_hanoi(n0, a0, b0):
    return f'{n0}:{a0}->{b0}'


def solv_hanoi(n0, a0, b0, c0):
    if n0 == 1:
        return [mov_hanoi(n0, a0, c0)]
    else:
        jit_sp_solv_hanoi = []
        for i in solv_hanoi(n0 - 1, a0, c0, b0):
            jit_sp_solv_hanoi.append(str(i))
        jit_sp_solv_hanoi.append(mov_hanoi(n0, a0, c0))
        for i in solv_hanoi(n0 - 1, b0, a0, c0):
            jit_sp_solv_hanoi.append(str(i) )
        return jit_sp_solv_hanoi


n, a, b, c = list(map(str,input().split()))
n_int = int(n)
js = solv_hanoi(n_int, a, b, c)
for j in js:
    print(j)
```



![局部截取_20251224_195916](D:\腾讯电脑管家截图文件\局部截取_20251224_195916.png)

```python
def zhajipai(js,k):
    js.sort(reverse=True)
    res = sum(js) / k
    if js[0] <= res:
        return res
    else:
        new_js = js[1:]
        nk = k-1
        return zhajipai(new_js,nk)

n,k0 = map(int,input().split())
js0 = list(map(int,input().split()))
print(f"{zhajipai(js0,k0):.3f}")
```



![局部截取_20251224_200025](D:\腾讯电脑管家截图文件\局部截取_20251224_200025.png)

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



![局部截取_20251224_200217](D:\腾讯电脑管家截图文件\局部截取_20251224_200217.png)

```python
def div(n0, k0):
    if k0 == 1:
        return 1
    elif k0 == 2:
        return n0 // 2
    else:
        res = 0
        i = 0
        while n0 - i * k0 - 1 >= 2:
            res += div(n0 - i * k0 - 1, k0 - 1)
            i += 1
        return res


def solve():
    n = int(input())
    sgm = 0
    for i in range(1, n + 1):
        sgm += div(n, i)
    print(sgm)


while True:
    try:
        if __name__ == '__main__':
            solve()
    except:
        break
```



![局部截取_20251224_200328](D:\腾讯电脑管家截图文件\局部截取_20251224_200328.png)

```python
def k0j(listy):
    return ''.join(listy)


def _2sqr(x0, y0, x1, y1):
    if abs(x0 - x1) == abs(y0 - y1):
        return True
    else:
        return False


def permute0(listy):
    if len(listy) == 1:
        return [[listy[0]]]
    else:
        al_listy = []
        for j_in_listy in listy:
            n_listy = [j_in_listy]
            listy0 = listy[:]
            listy0.remove(j_in_listy)
            for k_in_listyf in permute0(listy0):
                for k_in_listy in k_in_listyf:
                    n_listy.append(k_in_listy)
                al_listy.append(n_listy)
                n_listy = [j_in_listy]
        return al_listy


al = permute0([1, 2, 3, 4, 5, 6, 7, 8])
bl = []
for a in al:
    blacklist = 0
    for i in range(0, 7):
        if blacklist == 0:
            for j in range(i + 1, 8):
                if _2sqr(i + 1, int(a[i]), j + 1, int(a[j])):
                    blacklist = 1
                    break

    if blacklist == 0:
        bl.append(a)


res = []
for a in bl:
    aa = []
    for b in a:
        aa.append(str(b))
    res.append(aa)
res.sort()

Lne = int(input())
for _ in range(Lne):
    n = int(input())
    print(k0j(res[n - 1]))
```



<img src="D:\腾讯电脑管家截图文件\局部截取_20251224_200501.png" alt="局部截取_20251224_200501"  />

![局部截取_20251224_200517](D:\腾讯电脑管家截图文件\局部截取_20251224_200517.png)

```python
while True:
    n = int(input())
    if n == 0:
        break

    tj = list(map(int, input().split()))
    tj.sort()
    gw = list(map(int, input().split()))
    gw.sort()

    lt = 0
    rt = n - 1
    lg = 0
    rg = n - 1
    cnt = 0
    while lt <= rt:
        if tj[lt] > gw[lg]:
            cnt += 1
            lt += 1
            lg += 1
        elif tj[rt] > gw[rg]:
            cnt += 1
            rt -= 1
            rg -= 1
        else:
            if tj[lt] < gw[rg]:
                cnt -= 1
                
            lt += 1
            rg -= 1
            
    print(200 * cnt)
```



### 2.Special_Problems

![局部截取_20251224_194511](D:\腾讯电脑管家截图文件\局部截取_20251224_194511.png)

```python
text=input()
def swap_case(s):
    return ''.join(
        c.lower() if c.isupper() else
        c.upper() if c.islower() else
        c
        for c in s
    )
swapped=swap_case(text)
print(swapped)
```



![局部截取_20251224_194642](D:\腾讯电脑管家截图文件\局部截取_20251224_194642.png)

```python
l = int(input())
months = [0,31,28,31,30,31,30,31,31,30,31,30,31]
for x in range(1, l + 1):
    i, j, k, m, n = list(map(int,input().split()))
    sm = 0
    for t in range(i, m):
        sm += months[t]
    sd = n - j
    r = sm + sd
    num = k * 2 ** r
    print(num)
```



![局部截取_20251224_203951](D:\腾讯电脑管家截图文件\局部截取_20251224_203951.png)

```python
n = int(input())
btc = {}
for _ in range(n):
    card,m,d = input().split()
    m = int(m)
    d = int(d)
    b = (m,d)
    if b not in btc:
        btc[b] = []
    btc[b].append(card)
results = []
for b in sorted(btc.keys()):
    ss = btc[b]
    if len(ss) >= 2:
        result = f"{b[0]} {b[1]} " + " ".join(ss)
        results.append(result)
for r in results:
    print(r)
```



![局部截取_20251224_195405](D:\腾讯电脑管家截图文件\局部截取_20251224_195405.png)

```python
n=int(input())
o=oct(n)
print(o[2:])
```



![局部截取_20251224_204226](D:\腾讯电脑管家截图文件\局部截取_20251224_204226.png)

```python
l=int(input())
for t in range(l):
    n=int(input())
    i=0
    j=1
    for t in range(n//2):
        i+=j
        j+=i
    if n%2==1:
        print(j)
    else:
        print(i)
```



![局部截取_20251224_195227](D:\腾讯电脑管家截图文件\局部截取_20251224_195227.png)

```python
while True:
    try:
        n = input()
        if n == n[::-1]:
            print('YES')
        else:
            print('NO')
    except:
        break
```



![局部截取_20251224_202732](D:\腾讯电脑管家截图文件\局部截取_20251224_202732.png)

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



![局部截取_20251224_202631](D:\腾讯电脑管家截图文件\局部截取_20251224_202631.png)

```python
n = int(input())
if n == 0:
    print(1)
else:
    c = 1
    for i in range (n):
        c = c * (4 * i + 2) // (i + 2)
print(c)
```



![局部截取_20251224_201951](D:\腾讯电脑管家截图文件\局部截取_20251224_201951.png)

```python
print("%.2f" % abs(float(input())))
```



![局部截取_20251224_202911](D:\腾讯电脑管家截图文件\局部截取_20251224_202911.png)

```python
week = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
line = int(input())
for i in range(line):
    dt = input()
    c = int(dt[0:2])
    y = int(dt[2:4])
    m = int(dt[4:6])
    d = int(dt[6:8])
    if m <= 2:
        m += 12
        y -= 1
    if y == -1:
        y = 99
        c -= 1
    tw = y + y//4 + c//4 - 2*c + 26*(m+1)//10 + d - 1
    w = tw % 7
    print(week[w])
```



