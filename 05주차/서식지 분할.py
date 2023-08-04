n = int(input())
s = input()
score = 0
for i in range(1, n):
    left = s[:i]
    right = s[i:]
    score = max(score, len(set(left))+len(set(right)))
print(score)