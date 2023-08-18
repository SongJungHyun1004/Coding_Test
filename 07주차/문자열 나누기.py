def solution(s):
    answer = 0
    x = s[0]
    i = 1
    count_x = 1
    count_notx = 0
    if len(s) == 1:
        return 1
    while i < len(s):
        if s[i] == x:
            count_x += 1
        else:
            count_notx += 1
        if count_x == count_notx:
            count_x = 0
            count_notx = 0
            if i != len(s)-1:
                x = s[i+1]
            answer += 1
        elif i == len(s)-1:
            answer += 1
        i += 1 
    return answer