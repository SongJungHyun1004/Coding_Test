dxs = [0,-1,0,1]
dys = [1,0,-1,0]
result = "NO"
def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def dfs(i, j):
    global result
    visited[i][j] = True
    if i == n-1 and j == m-1:
        result = "YES"
        return
    for dx, dy in zip(dxs, dys):
        nx = i + dx
        ny = j + dy
        if in_range(nx, ny) and not visited[nx][ny]:
            dfs(nx, ny)
            
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
for i in range(n):
    for j in range(m):
        if grid[i][j] == '#':
            visited[i][j] = True
dfs(0, 0)
print(result)