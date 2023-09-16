from collections import deque

dxs = [0,-1,0,1]
dys = [1,0,-1,0]
def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs(i, j):
    q = deque([(i, j)])
    dist[i][j] = 0
    visited[i][j] = True
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if in_range(nx, ny) and not visited[nx][ny]:
                visited[nx][ny] = True
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
n, m = map(int, input().split())
grid = [
    []
    for _ in range(n)
]
for i in range(n):
    grid[i] = list(input())
visited = [
    [False]*m
    for _ in range(n)
]
dist = [
    [-1]*m
    for _ in range(n)
]
for i in range(n):
    for j in range(m):
        if grid[i][j] == '#':
            visited[i][j] = True
            dist[i][j] = -1
bfs(0, 0)
for i in range(n):
    print(*dist[i])