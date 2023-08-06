ans = []
result = []
def is_prime(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

def combi(cnt, begin, nums):
    if cnt == 3:
        result.append(sum(ans))
        return
    for i in range(begin, len(nums)):
        ans.append(nums[i])
        combi(cnt + 1, i + 1, nums)
        ans.pop()

def solution(nums):
    combi(0, 0, nums)
    i = 0
    while i < len(result):
        if not is_prime(result[i]):
            result.pop(i)
            i-=1
        i+=1
    answer = len(result)
    return answer