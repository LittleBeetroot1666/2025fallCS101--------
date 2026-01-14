js = list(map(int, input().split()))
js.sort()
if js[2] - js[0] <= 9:
    print(f'final {js[1]}')
else:
    print('check again')
