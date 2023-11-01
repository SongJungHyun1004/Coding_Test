n = int(input())
tile = [-1]*200001
p = 100000
for _ in range(n):
    x, c = input().split()
    x = int(x)
    if c == 'L':
        for _ in range(x):
            tile[p] = 0
            p -= 1
        p += 1
    elif c == 'R':
        for _ in range(x):
            tile[p] = 1
            p += 1
        p -= 1
print(tile.count(0), tile.count(1))