def solution(x, y, n):
    answer = 0
    nums = set()
    nums.add(x)
    while nums:
        if y in nums:
            return answer
        s = set()
        for i in nums:
            for j in [i+n, i*2, i*3]:
                if j <= y:
                    s.add(j)
        nums = s
        answer += 1

    return -1