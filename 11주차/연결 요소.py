def dfs(s):
    visited[s] = True
    for i in graph[s]:
        if not visited[i]:
            dfs(i)
    
n, m = map(int, input().split())
graph = [
    []
    for _ in range(n+1)
]
cc = 0 #connected component
visited = [False]*(n+1)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        cc += 1
print(cc)