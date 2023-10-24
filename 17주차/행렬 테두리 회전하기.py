def solution(rows, columns, queries):
    answer = []
    box = [
        [0]*(columns+1)
        for _ in range(rows+1)
    ]
    for i in range(1, rows+1):
        for j in range(1, columns+1):
            box[i][j] = (i-1)*columns+j
    for q in queries:
        x1, y1, x2, y2 = q[0], q[1], q[2], q[3]
        mn = 10001
        temp = box[x1][y1]
        mn = min(mn, temp)
        for i in range(x1+1, x2+1):
            box[i-1][y1] = box[i][y1]
            mn = min(mn, box[i-1][y1])
        for i in range(y1+1, y2+1):
            box[x2][i-1] = box[x2][i]
            mn = min(mn, box[x2][i-1])
        for i in range(x2-1, x1-1, -1):
            box[i+1][y2] = box[i][y2]
            mn = min(mn, box[i+1][y2])
        for i in range(y2-1, y1-1, -1):
            box[x1][i+1] = box[x1][i]
            mn = min(mn, box[x1][i+1])
        box[x1][y1+1] = temp
        answer.append(mn)
        
    return answer