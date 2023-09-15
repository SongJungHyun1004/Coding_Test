dxs = [0,-1,0,1]
dys = [1,0,-1,0]
def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def dfs(i, j):
    grid[i][j] = '.'
    for dx, dy in zip(dxs, dys):
        nx = i + dx
        ny = j + dy
        if in_range(nx, ny) and grid[nx][ny] != '.':
            dfs(nx, ny)
n, m = map(int, input().split())
grid = [
    []
    for _ in range(n)
]
for i in range(n):
    grid[i] = list(input())
cc = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] != '.':
            cc += 1
            dfs(i, j)
print(cc)