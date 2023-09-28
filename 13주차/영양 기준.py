def dfs(cnt, idx, choose):
    global case
    if cnt == choose:
        a, b, c = 0, 0, 0
        for i in range(n):
            if selected[i]:
                ai, bi, ci = foods[i]
                a += ai; b += bi; c += ci;
        if a <= x and b >= y and c <= z and a*4+b*4+c*9 <= m:
            case += 1
        return
    for i in range(idx, n):
        if not selected[i]:
            selected[i] = True
            dfs(cnt+1, i, choose)
            selected[i] = False
n = int(input())
foods = [
    []
    for _ in range(n)
]
for i in range(n):
    a, b, c = map(int, input().split())
    foods[i] = (a, b, c)
x, y, z, m = map(int, input().split())
selected = [False]*n
case = 0
for i in range(1, 4):
    dfs(0, 0, i)
print(case)