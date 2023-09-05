n, m = map(int, input().split())
adj = [
    []
    for _ in range(n)
]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u-1].append(v)
    adj[v-1].append(u)
for i in range(n):
    result = sorted(adj[i])
    if result:
        print(*result)
    else:
        print(-1)