n = int(input())
a = set(sorted(list(map(int, input().split()))))
b = set(sorted(list(map(int, input().split()))))
print("YES") if a == b else print("NO")