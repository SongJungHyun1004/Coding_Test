from itertools import permutations

def solution(word):
    answer = 0
    lst = ['A','E','I','O','U']*5
    perm = []
    for i in range(1, 6):
        perm += permutations(lst, i)
    temp = [''.join(p) for p in perm]
    perm = sorted(list(set(temp)))
    answer = perm.index(word)+1
    return answer