from collections import Counter

def solution(topping):
    answer = 0
    chulsu = Counter(topping)
    bro = set()
    for t in topping:
        chulsu[t] -= 1
        bro.add(t)
        if chulsu[t] == 0:
            del chulsu[t]
        if len(chulsu) == len(bro):
            answer += 1
    return answer