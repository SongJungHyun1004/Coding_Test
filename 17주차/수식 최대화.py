from itertools import permutations
def cal(n1, n2, op):
    if op == '*':
        return n1*n2
    elif op == '+':
        return n1+n2
    elif op == '-':
        return n1-n2
def solution(expression):
    answer = 0
    op = ['*','+','-']
    num = ''
    lst = []
    for i in expression:
        if i.isdigit():
            num += i
        else:
            lst.append(num)
            lst.append(i)
            num = ''
    lst.append(num)
    answer = -1
    for priority in list(permutations(op, 3)):
        lst2 = lst[:]
        for i in range(3):
            while True:
                try:
                    idx = lst2.index(priority[i])
                    num1 = int(lst2[idx-1])
                    num2 = int(lst2[idx+1])
                    temp = cal(num1, num2, priority[i])
                    lst2.pop(idx-1)
                    lst2.pop(idx-1)
                    lst2.pop(idx-1)
                    lst2.insert(idx-1, temp)
                except:
                    break
        answer = max(answer, abs(lst2[0]))
    return answer