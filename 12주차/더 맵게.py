from heapq import heappush, heappop, heapify

def solution(scoville, K):
    heapify(scoville)
    answer = 0
    while len(scoville) > 1:
        if scoville[0] >= K:
            return answer
        first = heappop(scoville)
        second = heappop(scoville)
        new = first + second*2
        heappush(scoville, new)
        answer += 1
    if scoville[0] >= K:
        return answer
    return -1