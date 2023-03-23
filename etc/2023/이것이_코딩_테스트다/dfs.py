# dfs 구현
# 깊이 우선 탐색 - stack 이용

def dfs(graph, v, visited):
    # 방문 처리
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        print("i: ", i)
        if not visited[i]:
            dfs(graph, i, visited)

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * len(graph)

dfs(graph, 1, visited)