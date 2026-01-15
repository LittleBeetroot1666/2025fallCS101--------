n = input()
k = int(input())

stack = []
for i in n:
    while stack and i < stack[-1] and k > 0:
        stack.pop()
        k -= 1
    stack.append(i)

if k > 0:
    print(int(''.join(stack[:-k])))
else:
    print(int(''.join(stack)))
