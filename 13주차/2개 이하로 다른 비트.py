def solution(numbers):
    answer = []
    for number in numbers:
        if number % 2 == 0:
            answer.append(number+1)
        else:
            x = list('0'+bin(number)[2:])
            fx = x[:]
            idx = ''.join(x).rfind('0')
            fx[idx] = '1'
            fx[idx+1] = '0'
            answer.append(int(''.join(fx), 2))
        
    return answer