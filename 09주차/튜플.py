def solution(s):
    answer = []
    temp_list = s[1:-1].split('},')
    tuple_list = []
    for t in temp_list:
        temp = t[1:].split(',')
        tuple_list.append(temp)
    tuple_list[-1][-1] = tuple_list[-1][-1][:-1] # 마지막 원소 '}' 제거
    tuple_list = sorted(tuple_list, key=lambda x: len(x)) # 길이로 정렬
    for tpl in tuple_list:
        tpl = map(int, tpl)
        for t in tpl:
            if not t in answer:
                answer.append(t)
                break
    return answer