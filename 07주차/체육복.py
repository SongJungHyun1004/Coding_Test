def solution(n, lost, reserve):
    answer = 0
    student = [1]*n
    for i in reserve:
        student[i-1] += 1
    for i in lost:
        student[i-1] -= 1
    for i in range(n):
        if student[i] == 2:
            if 0 <= i-1 and student[i-1] == 0:
                student[i-1] = 1
                student[i] = 1
            elif n > i+1 and student[i+1] == 0:
                student[i+1] = 1
                student[i] = 1
    student = [i for i in student if i != 0]
    answer = len(student)
    return answer