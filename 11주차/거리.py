from collections import deque

def bfs(start):
    q = deque([start])
    visited[start] = True
    while q:
        here = q.popleft()
        for there in graph[here]:
            if not visited[there]:
                visited[there] = True
                q.append(there)
                dist[there] = dist[here] + 1

n, m = map(int, input().split())
graph = [
    []
    for _ in range(n+1)
]
dist = [0]*(n+1)
visited = [0]*(n+1)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
bfs(1)
for i in range(1, n+1):
    print(dist[i], end=' ')