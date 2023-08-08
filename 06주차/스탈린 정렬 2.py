t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    stack = []
    for i in a:
        if (not stack) or stack[-1] < i:
            stack.append(i)
    print(*stack)