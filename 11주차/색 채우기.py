dxs = [0,-1,0,1]
dys = [1,0,-1,0]
def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def dfs(x, y):
    visited[x][y] = True
    grid[x][y] = '@'
    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        if in_range(nx, ny) and not visited[nx][ny]:
            dfs(nx, ny)
n, m = map(int, input().split())
x, y = map(int, input().split())
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
for i in range(n):
    for j in range(m):
        if grid[i][j] == '#':
            visited[i][j] = True
dfs(x-1, y-1)
for i in range(n):
    print(''.join(grid[i]))