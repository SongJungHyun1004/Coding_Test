def solution(n):
    floor = [0]*60000
    floor[0] = 1
    floor[1] = 2
    for i in range(2, n):
        floor[i] = (floor[i-1] + floor[i-2]) % 1000000007
    return floor[n-1]