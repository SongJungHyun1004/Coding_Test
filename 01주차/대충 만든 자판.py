def solution(keymap, targets):
    answer = []
    for target in targets:
        count = 0
        for t in target:
            n = 100
            for assign in keymap:
                temp = assign.find(t)
                if n > temp and temp != -1:
                    n = temp
            if n == 100:
                count = -1
                break
            count += (n+1)
        answer.append(count)
    return answer