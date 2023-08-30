def get_multiset(string):
    multi_set = []
    for i in range(len(string)):
        if i < len(string)-1:
            s = string[i:i+2]
            s = s.lower()
            if s.isalpha():
                multi_set.append(s)
    return multi_set

def solution(str1, str2):
    multi_set1 = sorted(get_multiset(str1))
    multi_set2 = sorted(get_multiset(str2))
    if not multi_set1 and not multi_set2:
        return 65536
    p1 = 0
    p2 = 0
    intersection = []
    union = []
    while p1 < len(multi_set1) and p2 < len(multi_set2):
        if multi_set1[p1] < multi_set2[p2]:
            union.append(multi_set1[p1])
            p1 += 1
        elif multi_set1[p1] > multi_set2[p2]:
            union.append(multi_set2[p2])
            p2 += 1
        else:
            intersection.append(multi_set1[p1])
            union.append(multi_set1[p1])
            p1 += 1
            p2 += 1
    if p1 < len(multi_set1):
        union.extend(multi_set1[p1:])
    elif p2 < len(multi_set2):
        union.extend(multi_set2[p2:])
    answer = int(len(intersection)/len(union)*65536)
    return answer