def solution(record):
    answer = []
    user = {}
    for info in record:
        inf = info.split()
        if inf[0] != 'Leave':
            user[inf[1]] = inf[2]
    for info in record:
        inf = info.split()
        if inf[0] == 'Enter':
            answer.append(user[inf[1]]+"님이 들어왔습니다.")
        if inf[0] == 'Leave':
            answer.append(user[inf[1]]+"님이 나갔습니다.")
    return answer