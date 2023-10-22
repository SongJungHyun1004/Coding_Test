def solution(book_time):
    answer = 0
    book_time = sorted(book_time)
    room = []
    
    for i, book in enumerate(book_time):
        sh, sm = book_time[i][0].split(':')
        eh, em = book_time[i][1].split(':')
        endtime = int(eh)*60+int(em)+10
        if not room:
            room.append([endtime])
        else:
            flag = 1
            for r in room:
                if r[-1] <= int(sh)*60+int(sm):
                    r.append(endtime)
                    flag = 0
                    break
            if flag:
                room.append([endtime])
    answer = len(room)
    return answer