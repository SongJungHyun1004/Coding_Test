from collections import deque

dxs = [0,-1,0,1]
dys = [1,0,-1,0]
line = 0
def in_range(x, y):
    return 0 <= x < n and 0<= y < m

def bfs(i, j):
    global line
    q = deque([(i, j)])
    while q:
        x, y = q.popleft()
        visited[x][y] = True
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if in_range(nx, ny):
                if grid[nx][ny] != '#':
                    line += 1
                if not visited[nx][ny]:
                    visited[nx][ny] = True
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
node = n*m
for i in range(n):
    for j in range(m):
        if grid[i][j] == '#':
            visited[i][j] = True
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            bfs(i, j)
print(node, line//2)