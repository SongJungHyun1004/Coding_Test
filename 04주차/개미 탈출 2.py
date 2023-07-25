t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    s = input()
    if s.find('O') < s.find('@'):
        s = s[::-1]
    start = s.find('@')
    end = s.find('O')
    s = s[start: end]
    count = s.count('#')
    print("NO" if count > m else "YES")
    if i != t-1:
        input()