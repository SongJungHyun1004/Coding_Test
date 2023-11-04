def manhattan_distance(pre, nxt):
    x, y = pre
    x2, y2 = nxt
    return abs(x-x2)+abs(y-y2)

n = int(input())
check = []
for _ in range(n):
    x, y = map(int, input().split())
    check.append((x, y))
lst = []
for i in range(1, n-1):
    dist = 0
    pre = check[0]
    for j in range(1, n-1):
        if i == j:
            continue
        dist += manhattan_distance(pre, check[j])
        pre = check[j]
    dist += manhattan_distance(pre, check[-1])
    lst.append(dist)
print(min(lst))