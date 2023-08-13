def canPronounce(word):
    a = 0; y = 0; w = 0; m = 0;
    i = 0
    while i < len(word):
        if word[i:i+3] == "aya":
            if a:
                return False
            a = 1
            i += 3
            y = 0; w = 0; m = 0;
        elif word[i:i+3] == "woo":
            if w:
                return False
            w = 1
            i += 3
            a = 0; y = 0; m = 0;
        elif word[i:i+2] == "ye":
            if y:
                return False
            y = 1
            i += 2
            a = 0; w = 0; m = 0;   
        elif word[i:i+2] == "ma":
            if m:
                return False
            m = 1
            i += 2
            a = 0; y = 0; w = 0;
        else:
            return False
    return True
            
def solution(babbling):
    answer = 0
    for word in babbling:
        if canPronounce(word):
            answer += 1
    return answer