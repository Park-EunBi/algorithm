import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, e = map(int, input().split())
graph = [
    []
    for _ in range(n + 1)
]


for _ in range(e):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))

v1, v2 = map(int, input().split())

def dijkstra(start, end):
    dist = [INF] * (n + 1)
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        time, node = heapq.heappop(q)
        if dist[node] < time:
            continue
        for b, w in graph[node]:
            cost = time + w
            if cost < dist[b]:
                dist[b] = cost
                heapq.heappush(q, (cost, b))
    return dist[end]
# v1, v2를 경로상에서 반드시 경유해야 한다
# 시작 -> v1 -> v2 -> 도착 (n)
# 시작 -> v2 -> v2 -> 도착 (n)
# 각 경로의 최소값을 더해주면 된다

path1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n)
path2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n)

# == 이 아니라 >= 로 해주어야 통과 (내가 설정한 inf 값을 넘을 수 있음)
if path1 >= INF or path2 >= INF:
    print(-1)
else:
    print(min(path1, path2))
