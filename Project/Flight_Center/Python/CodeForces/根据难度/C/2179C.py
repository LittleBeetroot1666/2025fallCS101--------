for _ in range(int(input())):
    n = int(input())
    js = list(map(int, input().split()))
    js.sort()
    print(max(js[0], js[1] - js[0]))
