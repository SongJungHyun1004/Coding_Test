t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    while True:
        moreRemove = False
        for i in range(1, len(a)):
            if a[i-1] > a[i]:
                a.pop(i)
                moreRemove = True
                break
        if not moreRemove:
            break
    print(*a)