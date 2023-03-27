# bfs
from collections import deque
def bfs(graph, start, visited):
    queue = deque([start]) # 초기화
    visited[start] = True # 방문 처리
    while queue: # 큐가 비워질 때 까지
        v = queue.popleft() # 하나씩 뽑기
        print(v, end=" ")
        for i in graph[v]: # 연결된 노드들을 방문해서
            if not visited[i]: # 방문하지 않은 노드이면
                queue.append(i) # 큐에 추가하고
                visited[i] = True # 방문 처리

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

bfs(graph, 1, visited)