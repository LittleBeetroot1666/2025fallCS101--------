line = input().strip()
inti = -1
while line[inti] == ' ' or line[inti] == '?':
    inti -= 1
if line[inti] == 'a' or line[inti] == 'A' or line[inti] == 'e' or line[inti] == 'E' or line[inti] == 'i' or line[inti] == 'I' or line[inti] == 'o' or line[inti] == 'O' or line[inti] == 'u' or line[inti] == 'U' or line[inti] == 'y' or line[inti] == 'Y':
    print('YES')
else:
    print('NO')
