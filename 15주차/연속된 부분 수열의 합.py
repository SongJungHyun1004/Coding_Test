def solution(sequence, k):
    answer = []
    interval_sum = 0
    end = 0
    mn = 1000000
    for start in range(len(sequence)):
        while interval_sum < k and end < len(sequence):
            interval_sum += sequence[end]
            end += 1
        
        if interval_sum == k:
            gap = end-1 - start
            if mn > gap:
                mn = gap
                answer = [start, end-1]
        interval_sum -= sequence[start]
    return answer