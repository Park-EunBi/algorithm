t = int(input())
for _ in range(t):
    n, m = map(int, input().split())

    # sol_1 - dfs
    graph = [
        []
        for _ in range(n + 1)
    ]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a) # 왕복 비행기

    visited = [0] * (n + 1)

    def dfs(node, cnt):
        visited[node] = 1
        for i in graph[node]:
            if not visited[i]:
                cnt = dfs(i, cnt + 1)
        return cnt

    result = dfs(1, 0)
    print(result)

    # sol_2
    # 모든 간선의 가중치가 같다면 최소 스패닝 트리의 간선 개수는 무조건 전체 노드 수 - 1
    print(n-1)