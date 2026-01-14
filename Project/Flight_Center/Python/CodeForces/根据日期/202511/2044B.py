def k0j(listy):
    return ''.join(listy)


for _ in range(int, input()):
    js = input()
    res = []
    for i in range(1, len(js) + 1):
        if js[-i] == 'p':
            res.append('q')
        elif js[-i] == 'q':
            res.append('p')
        else:
            res.append(js[-i])

    print(k0j(res))
