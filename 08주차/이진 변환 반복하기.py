def solution(s):
    answer = []
    zero_count = 0
    binary_convert = 0
    
    while s != '1':
        zero_count += s.count('0')
        s = s.replace('0', '')
        temp = bin(len(s))
        s = temp[2:]
        binary_convert += 1
    answer.append(binary_convert)
    answer.append(zero_count)
    return answer