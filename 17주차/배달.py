import heapq
def dijkstra(dist, adj):
    heap = []
    heapq.heappush(heap, [0, 1])
    while heap:
        cost, node = heapq.heappop(heap)
        for c, n in adj[node]:
            if c+cost < dist[n]:
                dist[n] = c+cost
                heapq.heappush(heap, [c+cost, n])
    
def solution(N, road, K):
    dist = [500001]*(N+1)
    dist[1] = 0
    adj = [
        []
        for _ in range(N+1)
    ]
    for r in road:
        a, b, c = r[0], r[1], r[2]
        adj[a].append((c, b))
        adj[b].append((c, a))
    dijkstra(dist, adj)
    answer = len([i for i in dist if K>=i])
    return answer