def solution(s):
    answer = ''
    s = sorted(list(map(int, s.split())))
    answer = str(s[0])+' '+str(s[-1])
    return answer 