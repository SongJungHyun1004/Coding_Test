def dfs(here, visited):
    visited[here] = True
    print(here, end=' ')
    for there in lst[here]:
        if not visited[there]:
            dfs(there, visited)

n, m = map(int, input().split())
lst = [
    []
    for _ in range(n+1)
]
visited = [False]*(n+1)
for _ in range(m):
    u, v = map(int, input().split())
    lst[u].append(v)
    lst[v].append(u)
for i in range(n):
    lst[i] = sorted(lst[i])
dfs(1, visited)