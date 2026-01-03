n, m = list(map(int, input().split()))
js = [i for i in range(1, n + 1)]
ts = [n * (n + 1) // 2 for n in range(1, n + 1)]
sgm = ts[-1]
m_rest = m % sgm
index = 0
while m_rest >= js[index]:
    m_rest -= js[index]
    index += 1
print(m_rest)
