name = input()
sex = []
for i in name:
    sex.append(i)
s = list(set(sex))
if len(s) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
