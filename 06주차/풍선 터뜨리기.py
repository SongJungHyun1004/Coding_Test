from collections import deque
n = int(input())
a = [0] + list(map(int, input().split()))
dq = deque([i for i in range(1, n+1)])
result = []
while True:
    i = dq.popleft()
    result.append(i)
    if not dq: break
    if a[i]>0:
        dq.rotate(-(a[i]-1))
    else:
        dq.rotate(abs(a[i]))
print(*result) 