s = list(input())
m = int(input())
i = 0
for _ in range(m):
    action = input()
    if action == "prev":
        if i != 0:
            i -= 1
    elif action == "next":
        if i+1 != len(s)-1:
            i += 1
    elif action == "left":
        if i != 0:
            s.pop(i)
            i -= 1
    elif action == "right":
         if i+1 != len(s)-1:
            s.pop(i+1)
print(s[i], s[i+1])