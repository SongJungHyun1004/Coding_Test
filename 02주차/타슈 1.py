t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    for _ in range(m):
        u, v = map(int, input().split())
        a[u-1] -= 1
        a[v-1] += 1
    print(*a)