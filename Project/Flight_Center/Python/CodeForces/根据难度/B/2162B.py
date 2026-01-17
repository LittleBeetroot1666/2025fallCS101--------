t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()

    if s == s[::-1]:
        print(0)

    zeros = [i + 1 for i in range(n) if s[i] == '0']
    ones = [i + 1 for i in range(n) if s[i] == '1']
    m = len(zeros)
    o = len(ones)
    found = False
    res = []

    for k in range(m + 1):
        for l in range(o + 1):
            if k + l == 0:
                continue
            p0 = zeros[:k]
            p1 = ones[-l:] if l > 0 else []
            p_indices = p0 + p1

            selected = set(p_indices)
            x = []
            for idx in range(n):
                if (idx + 1) not in selected:
                    x.append(s[idx])
            x_str = ''.join(x)
            if x_str == x_str[::-1]:
                print(len(p_indices))
                print(' '.join(map(str, p_indices)))
                found = True
                break
        if found:
            break
    if not found:
        print(-1)
