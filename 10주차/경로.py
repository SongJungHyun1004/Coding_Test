n, m = map(int, input().split())
lst = [
    []
    for _ in range(n)
]
for _ in range(m):
    u, v = map(int, input().split())
    lst[u-1].append(v)
    lst[v-1].append(u)
k = int(input())
a = list(map(int, input().split()))
for i in range(k-1):
    if a[i+1] not in lst[a[i]-1]:
        print("NO")
        exit(0)
print("YES")