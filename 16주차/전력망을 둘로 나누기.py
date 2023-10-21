def dfs(x, tree, visited):
    global node
    visited[x] = True
    node += 1
    for nx in tree[x]:
        if not visited[nx]:
            dfs(nx, tree, visited)
def solution(n, wires):
    answer = n
    global node
    graph = [
        []
        for _ in range(n+1)
    ]
    for i in range(n-1):
        u, v = wires[i][0], wires[i][1]
        graph[u].append(v)
        graph[v].append(u)
    tree = []
    for i in range(n-1):
        tree = [arr[:] for arr in graph]
        u, v = wires[i][0], wires[i][1]
        tree[u].remove(v)
        tree[v].remove(u)
        visited = [False]*(n+1)
        node = 0
        lst = []
        for j in range(1, n+1):
            if not visited[j]:
                dfs(j, tree, visited)
                lst.append(node)
                node = 0
        answer = min(answer, abs(lst[0]-lst[1]))
    return answer