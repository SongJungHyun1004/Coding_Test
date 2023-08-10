n, m = map(int, input().split())
stack = [i for i in range(1, n+1)]
for _ in range(m):
    num = int(input())
    if num == 1:
        stack.append(stack[0])
        stack.pop(0)
    else:
        if len(stack) != 1:
            stack.pop(0)
        else:
            break
print(stack[0])