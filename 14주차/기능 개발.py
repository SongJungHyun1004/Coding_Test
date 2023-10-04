import math
def solution(progresses, speeds):
    answer = []
    works = []
    for i in range(len(speeds)):
        works.append(math.ceil(((100-progresses[i])/speeds[i])))
    stack = []
    deploy = 1
    for work in works:
        if stack:
            if stack[-1] < work:
                stack.pop()
                stack.append(work)
                answer.append(deploy)
                deploy = 1
            else:
                deploy += 1
        else:
            stack.append(work)
    answer.append(deploy)
    return answer