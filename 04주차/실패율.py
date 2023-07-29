def solution(N, stages):
    answer = []
    stages = sorted(stages)
    for curStage in range(1, N+1):
        fail = 0
        for user in range(len(stages)):
            if curStage >= stages[user]:
                fail += 1
            else:
                break
        if len(stages):
            fail_rate = fail/len(stages)
        else:
            fail_rate = 0
        stages = stages[fail:]
        answer.append([curStage, fail_rate])
    answer = sorted(answer, key = lambda x: x[1], reverse=True)
    answer = [i[0] for i in answer]
    return answer