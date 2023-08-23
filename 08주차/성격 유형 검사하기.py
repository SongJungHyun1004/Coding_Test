def complete_mbti(a, b, mbti_dict, mbti):
    if mbti_dict[a] < mbti_dict[b]:
        mbti += b
    else:
        mbti += a
    return mbti

def solution(survey, choices):
    answer = ''
    mbti_dict = dict(zip('RTCFJMAN', [0 for _ in range(8)]))
    
    for s, c in zip(survey, choices):
        if c < 4:
            mbti_dict[s[0]] += 4-c
        elif c > 4:
            mbti_dict[s[1]] += c-4
        else:
            continue
    answer = complete_mbti('R', 'T', mbti_dict, answer)
    answer = complete_mbti('C', 'F', mbti_dict, answer)
    answer = complete_mbti('J', 'M', mbti_dict, answer)
    answer = complete_mbti('A', 'N', mbti_dict, answer)
    return answer