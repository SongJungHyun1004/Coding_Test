def solution(ingredient):
    hamburger = []
    answer = 0
    for i in ingredient:
        hamburger.append(i)
        if hamburger[-4:] == [1,2,3,1]:
            del hamburger[-4:]
            answer += 1
        
    return answer