n, m = map(int, input().split())
a = list(map(int, input().split()))
for _ in range(m):
    l, r = map(int, input().split())
    s = 0
    for i in range(l-1, r):
        s += a[i]
    print(s)