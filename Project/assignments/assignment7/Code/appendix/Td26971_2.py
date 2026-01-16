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
