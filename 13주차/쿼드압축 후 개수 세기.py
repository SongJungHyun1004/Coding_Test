def compress(arr):
    global zero
    global one
    n = len(arr)
    count = 0
    for i in range(n):
        count += arr[i].count(arr[0][0])
    if count == n*n:
        if arr[0][0] == 0:
            zero += 1
        else:
            one += 1
        return
    compress([row[:n//2] for row in arr[:n//2]])
    compress([row[:n//2] for row in arr[n//2:]]) 
    compress([row[n//2:] for row in arr[:n//2]]) 
    compress([row[n//2:] for row in arr[n//2:]]) 

def solution(arr):
    global zero
    global one
    zero = 0
    one = 0
    compress(arr)
    answer = [zero, one]
    return answer