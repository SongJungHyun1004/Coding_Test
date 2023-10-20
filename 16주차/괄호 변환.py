def flip(u):
    dic = {'(':')', ')':'('}
    return ''.join([dic[i] for i in u])
    
def is_correct(p):
    stack = []
    for i in p:
        if i == '(':
            stack.append('(')
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return False
    return True
    
def seperate(w):
    for i in range(2, len(w), 2):
        u = w[:i]
        if u.count('(') == u.count(')'):
            return u, w[i:]
    return w, ""
def correct(w):
    if not w:
        return ""
    u, v = seperate(w)
    if is_correct(u):
        return u + correct(v)
    else:
        result = '(' + correct(v) + ')'
        u = flip(u[1:-1])
        return result + u
    
def solution(p):
    answer = ''
    answer = correct(p)
    return answer