from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0]*bridge_length)
    q = deque(truck_weights)
    current_weight = 0
    while q:
        time += 1
        current_weight -= bridge.popleft()
        if current_weight + q[0] <= weight:
            current_weight += q[0]
            bridge.append(q.popleft())
        else:
            bridge.append(0)
    time += bridge_length
        
    return time