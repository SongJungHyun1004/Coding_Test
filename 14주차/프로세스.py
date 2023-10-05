from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque([(i, p) for i, p in enumerate(priorities)])
    while q:
        process = q.popleft()
        if any(process[1] < qq[1] for qq in q):
            q.append(process)
        else:
            answer += 1
            if process[0] == location:
                return answer