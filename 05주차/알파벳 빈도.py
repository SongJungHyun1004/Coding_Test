n, m = map(int, input().split())
s = input()
for _ in range(m):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    temp = s[l:r+1]
    print(temp.count('e'))