t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a = a[::-1]
    for i in range(1, n):
        while a[i] > a[i-1]:
            a[i] = a[i]//2
    a = a[::-1]
    print(*a)