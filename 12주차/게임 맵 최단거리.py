from collections import deque
dxs = [0,-1,0,1]
dys = [1,0,-1,0]
def in_range(x, y):
    global n, m
    return 0 <= x < n and 0 <= y < m
def bfs(i, j, maps):
    global n, m
    q = deque([(i, j)])
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if in_range(nx, ny) and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1 
                q.append((nx, ny))
    return maps[n-1][m-1]

def solution(maps):
    global n, m
    n = len(maps)
    m = len(maps[0])
    answer = bfs(0, 0, maps)
    if answer == 1:
        answer = -1
    return answer