n, m = map(int, input().split())
queue = [i for i in range(1, n+1)]
for _ in range(m):
    num = int(input())
    if num == 1:
        queue.append(queue[0])
        queue.pop(0)
    else:
        if len(queue) != 1:
            queue.pop(0)
        else:
            break
print(queue[0])