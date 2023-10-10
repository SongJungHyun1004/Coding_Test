from collections import deque

def solution(order):
    answer = 0
    q = deque(order)
    stack = []
    for i in range(1, len(order)+1):
        stack.append(i)
        while stack and stack[-1] == q[0]:
            answer += 1
            stack.pop()
            q.popleft()
    return answer