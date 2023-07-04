s = input()
answer = ''
for i in s:
    if i.islower():
        answer += i.upper()
    else:
        answer += i.lower()

print(answer)