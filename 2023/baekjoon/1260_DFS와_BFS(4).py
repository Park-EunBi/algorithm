from collections import deque
n, m, v = map(int, input().split())
graph = [
    []
    for _ in range(n + 1)
]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for g in graph:
    g.sort()


def dfs(graph, num, visited):
    # 방문 처리
    visited[num] = True
    print(num, end = ' ')

    for g in graph[num]:
        if not visited[g]:
            dfs(graph, g, visited)

def bfs(graph, start, visited):
    # 선언
    q = deque()
    # 초기화
    q.append(start)
    visited[start] = True
    # 반복
    while q:
        c = q.popleft()
        print(c, end = ' ')
        for g in graph[c]:
            if not visited[g]:
                q.append(g)
                visited[g] = True

# main
visited = [False] * (n + 1)
dfs(graph, v, visited)
print()
visited = [False] * (n + 1)
bfs(graph, v, visited)
