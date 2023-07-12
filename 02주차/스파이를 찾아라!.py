t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    first = a[0]
    if a.count(first) == 1:
        print(1)
    else:
        for i in range(1, n):
            if a[i] != first:
                print(i+1)
                break