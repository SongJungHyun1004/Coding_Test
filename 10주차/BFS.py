from collections import deque

def bfs(start):
    q = deque([start])
    while q:
        here = q.popleft()
        visited[here] = True
        print(here, end=' ')
        for there in graph[here]:
            if not visited[there]:
                q.append(there)
                visited[there] = True
n, m = map(int, input().split())
graph = [
    []
    for _ in range(n+1)
]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for i in range(n):
    graph[i] = sorted(graph[i])

visited = [False]*(n+1)
bfs(1)