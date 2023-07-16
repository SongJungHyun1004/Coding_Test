def solution(s, skip, index):
    answer = ''
    for i in s:
        count = 0
        p = ord(i)
        while count < index:
            p += 1
            if chr(p) > 'z':
                p -= 26
            if chr(p) not in skip:
                count += 1
        answer += chr(p)
    return answer