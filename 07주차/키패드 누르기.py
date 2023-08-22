def getIndex2d(lst, n):
    for i in range(len(lst)):
        if n in lst[i]:
            return [i, lst[i].index(n)]

def solution(numbers, hand):
    keyPad =[
        ['1','2','3'],
        ['4','5','6'],
        ['7','8','9'],
        ['*','0','#']
    ]
    leftThumb = '*'
    rightThumb = '#'
    answer = ''
    for n in numbers:
        if n == 1 or n == 4 or n == 7:
            leftThumb = str(n)
            answer += 'L'
        elif n == 3 or n == 6 or n == 9:
            rightThumb = str(n)
            answer += 'R'
        else:
            left = getIndex2d(keyPad, leftThumb)
            right = getIndex2d(keyPad, rightThumb)
            mid = getIndex2d(keyPad, str(n))
            left_dist = abs(mid[0]-left[0]) + mid[1]-left[1]
            right_dist = abs(mid[0]-right[0]) + right[1]-mid[1]
            if left_dist < right_dist:
                leftThumb = str(n)
                answer += 'L'
            elif right_dist < left_dist:
                rightThumb = str(n)
                answer += 'R'
            else:
                if hand == 'left':
                    leftThumb = str(n)
                    answer += 'L'
                else:
                    rightThumb = str(n)
                    answer += 'R'
    return answer