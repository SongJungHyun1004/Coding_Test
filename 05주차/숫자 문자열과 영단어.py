def solution(s):
    num_dic = {
        'zero'  : '0',
        'one'   : '1',
        'two'   : '2',
        'three' : '3',
        'four'  : '4',
        'five'  : '5',
        'six'   : '6',
        'seven' : '7',
        'eight' : '8',
        'nine'  : '9'
    }
    for eng, num in num_dic.items():
        s = s.replace(eng, num)
    answer = int(s)
    return answer