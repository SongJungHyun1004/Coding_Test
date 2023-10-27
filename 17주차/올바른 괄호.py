def solution(s):
    answer = True
    
    stack = []
    for i in s:
        if stack and i == ')':
            stack.pop()
        elif i == '(':
            stack.append(i)
        else:
            return False
    if stack:
        return False

    return True