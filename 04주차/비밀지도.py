def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        temp1 = format(i, 'b').zfill(n)
        temp2 = format(j, 'b').zfill(n)
        wall = ""
        for a, b in zip(temp1, temp2):
            if a == '0' and b == '0':
                wall += " "
            else:
                wall += "#"
        answer.append(wall)
    return answer