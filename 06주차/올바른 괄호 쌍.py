s = input()
stack = []
for i in s:
    if i == '(':
        stack.append(i)
    else:
        if stack:
            stack.pop()
        else:
            print("NO")
            exit(0)
print("NO" if stack else "YES")