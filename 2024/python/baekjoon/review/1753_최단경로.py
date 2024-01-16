import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
start = int(input())

graph = [
    []
    for _ in range(v + 1)
]
dist = [INF] * (v + 1)

for _ in range(e):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # time, node
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

dijkstra(start)
for i in range(1, v + 1):
    if dist[i] >= INF:
        print('INF')
    else:
        print(dist[i])