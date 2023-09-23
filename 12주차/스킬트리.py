def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        n = 0
        flag = 1
        for j in i:
            try:
                learn = skill[n]
            except:
                break
            
            if j in skill:
                if j != learn:
                    flag = 0
                    break
                else:
                    n += 1
        if flag:
            answer += 1
            
    return answer