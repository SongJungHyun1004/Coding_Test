def solution(dartResult):
    answer = 0
    score = []
    for i in range(len(dartResult)):
        if dartResult[i].isdigit():
            if dartResult[i] == '1' and dartResult[i+1] == '0':
                score.append(10)
            else:
                if not (i > 0 and dartResult[i] == '0' and dartResult[i-1] == '1'):
                    score.append(int(dartResult[i]))
        elif dartResult[i] == 'D':
            temp = score.pop() ** 2
            score.append(temp)
        elif dartResult[i] == 'T':
            temp = score.pop() ** 3
            score.append(temp)
        elif dartResult[i] == '*':
            temp = score.pop()*2
            if len(score) > 0: 
                temp2 = score.pop()*2
                score.append(temp2)
            score.append(temp)
        elif dartResult[i] == '#':
            temp = score.pop() * -1
            score.append(temp)
    answer = sum(score)
    return answer