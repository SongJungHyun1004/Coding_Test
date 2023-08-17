def solution(participant, completion):
    answer = ''
    participant = sorted(participant)
    completion = sorted(completion)
    last_participant = participant.pop()
    for p, c in zip(participant, completion):
        if p != c:
            answer = p
            break
    if answer == '':
        answer = last_participant
    return answer