s = input()
t = input()
ps = 0
pt = 0
while True:
    if t[pt] == s[ps]:
        pt += 1
    ps += 1
    if pt == len(t):
        print("YES")
        break
    if ps == len(s):
        print("NO")
        break