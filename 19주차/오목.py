n = 19
pan = [
    list(map(int, input().split()))
    for _ in range(n)
]

def in_range(x, y):
    return 0<=x<n and 0<=y<n

def check_win(x, y, dx, dy, current):
    for i in range(1, 5):
        nx, ny = x+i*dx, y+i*dy
        if not in_range(nx, ny) or pan[nx][ny] != current:
            return False
    return True
    
def find_winner():
    for x in range(n):
        for y in range(n):
            if pan[x][y] == 1 or pan[x][y] == 2:
                dxs = [0,1,1,1]
                dys = [1,0,1,-1]
                for dx, dy in zip(dxs, dys):
                    if check_win(x, y, dx, dy, pan[x][y]):
                        return pan[x][y], x+dx*2, y+dy*2
    return 0, None, None

winner, x, y = find_winner()
if winner:
    print(winner)
    print(x+1, y+1)
else:
    print(0)