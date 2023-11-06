from itertools import combinations
def isCarry(n1, n2, n3):
    max_len = len(str(max(n1, n2, n3)))
    for i in range(1, max_len+1):
        rm1 = n1%(10**i)//(10**(i-1))
        rm2 = n2%(10**i)//(10**(i-1))
        rm3 = n3%(10**i)//(10**(i-1))
        if rm1+rm2+rm3 >= 10:
            return True
    return False

n = int(input())
num_lst = []
for _ in range(n):
    num_lst.append(int(input()))
combi = list(combinations(num_lst, 3))
mx = float('-inf')
for i in combi:
    n1, n2, n3 = i
    if not isCarry(n1, n2, n3):
        mx = max(mx, n1+n2+n3)
print(mx) if not mx == float('-inf') else print(-1)