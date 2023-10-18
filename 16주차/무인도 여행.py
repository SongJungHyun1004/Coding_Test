import sys
sys.setrecursionlimit(10**5)
dxs = [0,-1,0,1]
dys = [1,0,-1,0]
box, visited = [], []
area, n, m = 0, 0, 0
def in_range(x, y):
    global n, m
    return 0<=x<n and 0<=y<m
def dfs(x, y):
    global area, visited, box
    visited[x][y] = True
    area += int(box[x][y])
    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        if in_range(nx, ny) and not visited[nx][ny] and box[nx][ny] != 'X':
            dfs(nx, ny)
    
def solution(maps):
    global area, visited, box, n, m
    box = maps
    n = len(maps)
    m = len(maps[0])
    visited = [
        [False]*m
        for _ in range(n)
    ]
    answer = []
    for i in range(n):
        for j in range(m):
            if box[i][j] != 'X' and not visited[i][j]:
                dfs(i, j)
                answer.append(area)
                area = 0
    if not answer:
        return [-1]
    return sorted(answer)