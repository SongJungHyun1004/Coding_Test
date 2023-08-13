def solution(lottos, win_nums):
    possible = lottos.count(0)
    lottos = set(lottos)
    win_nums = set(win_nums)
    minimum = lottos.intersection(win_nums)
    
    answer = []
    high = 7-(len(minimum)+possible)
    low = 7-(len(minimum))
    if high == 7:
        high = 6
    if low == 7:
        low = 6
    answer.append(high)
    answer.append(low)
    return answer