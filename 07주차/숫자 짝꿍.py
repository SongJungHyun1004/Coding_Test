def solution(X, Y):
    answer = ''
    x = [0]*10
    y = [0]*10
    common = []
    for i in range(10):
        x[i] = X.count(str(i))
        y[i] = Y.count(str(i))
        mn = min(x[i], y[i])
        for _ in range(mn):
            common.append(i)

    result = sorted(common, reverse = True)
    if len(result):
        if result[0] == 0:
            answer = '0'
        else:
            answer = ''.join(map(str, result))
    else:
        answer = '-1'
    return answer