n = int(input())
a = list(map(int, input().split()))
answer = []
for i in range(n):
    answer.append(sum(a[:i+1]))
print(*answer)