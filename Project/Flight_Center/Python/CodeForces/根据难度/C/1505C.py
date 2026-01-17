w = input()
js = []
for lt in w:
    js.append(lt)
blacklist = 0
for i in range(0, len(js)-2):
    if ord(js[i])+ord(js[i+1]) == ord(js[i+2])+65 or ord(js[i])+ord(js[i+1])==ord(js[i+2])+91:
        blacklist += 0
    else:
        blacklist += 1
if blacklist == 0:
    print("YES")
else:
    print("NO")