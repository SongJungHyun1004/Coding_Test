class G:
    rm = set()
    bombed = 0
    board = []


def bomb():
    for i, j in reversed(sorted(G.rm)):
        G.board[i].pop(j)
        G.bombed += 1
    G.rm = set()


def search(i, j):
    if j >= len(G.board[i+1]) - 1:
        return

    if G.board[i][j] == G.board[i][j+1] == G.board[i+1][j] == G.board[i+1][j+1]:
        for x, y in [(i + 1, j + 1), (i + 1, j), (i, j + 1), (i, j)]:
            G.rm.add((x, y))


def solution(m, n, board):
    G.board = [[board[i][j] for i in reversed(range(m))] for j in range(n)]
    
    while True:
        for i in range(len(G.board) - 1):
            for j in range(len(G.board[i]) - 1):
                search(i, j)
        if not G.rm:
            break
        bomb()
    return G.bombed