def fight_loose(atk_j, atk_m, hp_m):
    global hp_j
    while True:
        hp_m -= atk_j
        if hp_m <= 0:
            return False
        hp_j -= atk_m
        if hp_j <= 0:
            return True

t = int(input())
for i in range(t):
    n, m, k = map(int, input().split())
    m2 = m
    s = input()
    pos_j = s.find('@')
    atk_j, hp_j = map(int, input().split())
    hp_j2 = hp_j
    monsters = [-1]*n
    for _ in range(k):
        pos_m, atk_m, hp_m = map(int, input().split())
        monsters[pos_m-1] = (atk_m, hp_m)
    canEscape = False
    move_right_point = pos_j
    if move_right_point < n-1:
        move_right_point += 1
    while True:
        if s[move_right_point] == 'O':
            canEscape = True
            break
        if move_right_point == n-1:
            canEscape = False
            break
        if s[move_right_point] == '#':
            if m:
                m -= 1
            else:
                canEscape = False
                break
        if s[move_right_point] == '&':
            atk_m, hp_m = monsters[move_right_point]
            if fight_loose(atk_j, atk_m, hp_m):
                canEscape = False
                break
        move_right_point += 1
    if canEscape:
        print("YES")
    else:
        hp_j = hp_j2
        m = m2
        move_left_point = pos_j
        if move_left_point > 0:
            move_left_point -= 1
        while True:
            if s[move_left_point] == 'O':
                canEscape = True
                break
            if move_left_point == 0:
                canEscape = False
                break
            if s[move_left_point] == '#':
                if m:
                    m -= 1
                else:
                    canEscape = False
                    break
            if s[move_left_point] == '&':
                atk_m, hp_m = monsters[move_left_point]
                if fight_loose(atk_j, atk_m, hp_m):
                    canEscape = False
                    break
            move_left_point -= 1
        if canEscape:
            print("YES")
        else:
            print("NO")
    if i != t - 1:
        input()