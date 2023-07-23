def solution(t, p):
    answer = 0
    word = len(p)
    for i in range(len(t)-word+1):
        if int(t[i:i+word]) <= int(p):
            answer += 1
    return answer