def solution(board, moves):
    answer = 0
    n = len(board[0])
    basket = []
    for m in moves:
        for i in range(n):
            if board[i][m-1] != 0:
                if len(basket) > 0 and board[i][m-1] == basket[-1]:
                    basket.pop()
                    answer += 2
                else:
                    basket.append(board[i][m-1])
                board[i][m-1] = 0
                break
    return answer