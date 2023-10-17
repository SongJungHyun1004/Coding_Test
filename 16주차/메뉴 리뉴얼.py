from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for i in course:
        temp = []
        for order in orders:
            temp += combinations(sorted(order), i)
        counter = Counter(temp)
        if counter and max(counter.values()) != 1:
            answer += [''.join(k) for k in counter if counter[k] == max(counter.values())]
    return sorted(answer)