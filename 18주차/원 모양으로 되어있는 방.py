n = int(input())
room = [0]*n
for i in range(n):
    room[i] = int(input())
mn = float('inf')
for i in range(n):
    dist = 0
    for j in range(n):
        p = i+j
        if p >= n:
            p -= n
        dist += j*room[p]
    mn = min(mn, dist)
print(mn)