sentence1 = input()
sentence2 = input()
st1 = sentence1.lower()
st2 = sentence2.lower()
p1 = p2 = 0
blacklist = 0
for i in range(0, len(sentence1)):
    p1 = st1[i]
    p2 = st2[i]
    if p1 > p2:
        print("1")
        blacklist = 1
        break
    elif p2 > p1:
        print("-1")
        blacklist = 1
        break
if blacklist == 0:
    print("0")
