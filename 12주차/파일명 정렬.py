import re
def solution(files):
    answer = []
    temp = []
    for file in files:
        temp.append(re.split(r"([0-9]+)", file))
    temp = sorted(temp, key=lambda x: (x[0].lower(),int(x[1])))
    answer = [''.join(t) for t in temp]
    return answer