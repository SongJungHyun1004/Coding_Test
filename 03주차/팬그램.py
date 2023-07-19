s = input()
for i in range(ord('a'), ord('z')+1):
    n = s.count(chr(i))
    if n < 1:
        print("NO")
        exit(0)
print("YES")