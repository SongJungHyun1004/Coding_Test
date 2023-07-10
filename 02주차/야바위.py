n, m = map(int, input().split())
lst = [0]*n
for i in range(1, n+1):
    lst[i-1] = i
for i in range(m):
    u, v = map(int, input().split())
    lst[u-1], lst[v-1] = lst[v-1], lst[u-1]
print(*lst)