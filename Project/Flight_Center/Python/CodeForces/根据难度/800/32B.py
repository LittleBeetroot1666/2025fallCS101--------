line = input()
res = []
init = 0
while init <= len(line) - 1:
    if line[init] == '.':
        res.append('0')
        init += 1
    else:
        if line[init + 1] == '.':
            res.append('1')
            init += 2
        else:
            res.append('2')
            init += 2

print(''.join(res))
