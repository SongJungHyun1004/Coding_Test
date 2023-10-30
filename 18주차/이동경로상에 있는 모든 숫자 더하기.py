dxs = [0,1,0,-1]
dys = [1,0,-1,0]
def in_range(x, y):
    return 0<=x<n and 0<=y<n
def move(x, y, d, s):
    summation = grid[x][y]
    for i in s:
        if i == 'R':
            d += 1
            d %= 4
        elif i == 'L':
            d -= 1
            if d < 0:
                d = 3
        else:
            nx = x + dxs[d]
            ny = y + dys[d]
            if in_range(nx, ny):
                summation += grid[nx][ny]
                x = nx
                y = ny
    return summation
n, t = map(int, input().split())
s = input()
grid = [
    []
    for _ in range(n)
]
for i in range(n):
    grid[i] = list(map(int, input().split()))
d = 3
print(move(n//2, n//2, d, s))