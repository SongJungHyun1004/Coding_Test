def solution(new_id):
    temp = ''
    for i in new_id:
        temp += i.lower()
    temp2 = ''
    for i in temp:
        if i.islower() or i.isdigit() or i == '-' or i == '_' or i == '.':
            temp2 += i
    temp3 = ''
    for i in temp2:
        if len(temp3) == 0 or not (len(temp3) and temp3[-1] == '.' and i == '.'):
            temp3 += i
    temp4 = temp3
    while temp4.startswith('.') or temp4.endswith('.'):
        if temp4.startswith('.'):
            temp4 = temp4[1:]
        if temp4.endswith('.'):
            temp4 = temp4[:-1]
    temp5 = ''
    if len(temp4) == 0:
        temp5 = 'a'
    else:
        temp5 = temp4
    temp6 = ''
    if len(temp5) > 15:
        temp6 = temp5[:15]
        if temp6[-1] == '.':
            temp6 = temp6[:-1]
    else:
        temp6 = temp5
    answer = temp6
    while len(answer) < 3:
        answer += temp6[-1]
    return answer