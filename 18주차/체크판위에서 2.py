r, c = map(int, input().split())
board = [
    input().split()
    for _ in range(r)
]
cnt = 0
for i in range(1, r):
    for j in range(1, c):
        for k in range(i+1, r-1):
            for l in range(j+1, c-1):
                if board[0][0] != board[i][j] and board[i][j] != board[k][l] and board[k][l] != board[-1][-1]:
                    cnt += 1
print(cnt)