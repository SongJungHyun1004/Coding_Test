def solution(today, terms, privacies):
    today = list(map(int, today.split('.')))
    term_dic = {}
    for i in range(len(terms)):
        key, value = terms[i].split()
        term_dic[key] = int(value)

    answer = []
    for i in range(len(privacies)):
        getDay, term = privacies[i].split()
        getDay = list(map(int, getDay.split('.')))
        expDay = getDay[:]
        expDay[1] += term_dic[term]
        expDay[2] -= 1
        if expDay[2] == 0:
            expDay[2] = 28
            expDay[1] -= 1
        expDay[0] += expDay[1] // 12
        expDay[1] = expDay[1] % 12
        if expDay[1] == 0:
            expDay[1] = 12
            expDay[0] -= 1
            
        for j in range(3):
            if today[j] > expDay[j]:
                answer.append(i+1)
                break
            elif today[j] < expDay[j]:
                break
    return answer