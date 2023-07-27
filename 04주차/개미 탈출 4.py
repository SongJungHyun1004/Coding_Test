def canEscape(m, atk_j, hp_j, atk_m, hp_m, temp_s):
    hole = temp_s.find('O')
    if hole != -1:
        right_s = temp_s[:hole]
        if right_s.count('#') <= m:
            if '&' in right_s:
                while True:
                    hp_m -= atk_j
                    if hp_m <= 0:
                        return True
                    hp_j -= atk_m
                    if hp_j <= 0:
                        break
            else:
                return True
    return False
t = int(input())
for i in range(t):
    e = False
    n, m = map(int, input().split())
    s = input().replace('.', '')
    atk_j, hp_j = map(int, input().split())
    atk_m, hp_m = map(int, input().split())
    j = s.find('@')
    temp_right_s = s[j:]
    temp_left_s = s[:j]
    if canEscape(m, atk_j, hp_j, atk_m, hp_m, temp_right_s):
        print("YES")
    elif canEscape(m, atk_j, hp_j, atk_m, hp_m, temp_left_s[::-1]):
        print("YES")
    else:
        print("NO")

    if i != t - 1:
        input()