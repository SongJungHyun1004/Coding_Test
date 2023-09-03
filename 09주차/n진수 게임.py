def convert(num, n):
    T = "0123456789ABCDEF"
    q, r = divmod(num, n)
    return convert(q, n) + T[r] if q else T[r]

def solution(n, t, m, p):
    answer = ''
    total = ''
    num = 0
    while len(total) < t*m:
        total += convert(num, n)
        num += 1
    for i in range(p-1, t*m, m):
        answer += total[i]
        
    return answer