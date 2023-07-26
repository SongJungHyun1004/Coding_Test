t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    s = input().replace('.', '')
    if s.find('O') < s.find('@'):
        s = s[::-1]
    start = s.find('@')
    start_left = start - (m+1)
    if start_left < 0:
        start_left = 0
    start_right = start + (m+1)
    if start_right > len(s)-1:
        start_right = len(s)-1
    temp = s[start_left:start_right+1]
    if 'G' in temp or 'O' in temp:
        print("YES")
    else:
        print("NO")
    if i != t-1:
        input()