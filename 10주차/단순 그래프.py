n, m = map(int, input().split())
lst = []
for _ in range(m):
    u, v = map(int, input().split())
    if u == v:
        print("NO")
        exit(0)
    if not lst or not sorted([u, v]) in lst:
        lst.append(sorted([u, v]))
    else:
        print("NO")
        exit(0)
print("YES")