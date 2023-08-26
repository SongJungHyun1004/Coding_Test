def is_correct_s(s):
    stack = []
    for i in s:
        if i == '(' or i == '{' or i == '[':
            stack.append(i)
        if i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return False
        if i == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                return False
        if i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                return False
    if stack:
        return False
    else:
        return True

def solution(s):
    answer = 0
    for i in range(len(s)):
        sliding_s = s[i:]+s[:i]
        if is_correct_s(sliding_s):
            answer += 1
    return answer