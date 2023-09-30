dxs = [0,-1,0,1]
dys = [1,0,-1,0]
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n
def dfs(i, j, move, score):
    if move == m:
        return lst.append(score)
    for dx, dy in zip(dxs, dys):
        nx = i + dx
        ny = j + dy
        if in_range(nx, ny):
            dfs(nx, ny, move+1, score+grid[nx][ny])
n, m = map(int, input().split())
grid = [
    []
    for _ in range(n)
]
for i in range(n):
    grid[i] = list(map(int, input().split()))
mn = 1000
for i in range(n):
    for j in range(n):
        lst = []
        dfs(i, j, 0, 0)
        mn = min(mn, max(lst))
print(mn)