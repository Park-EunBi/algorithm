import heapq
import sys
from collections import defaultdict

input = sys.stdin.readline

V, e = map(int, input().split())
start = int(input())

graph = defaultdict(list)
dist = defaultdict(int)

for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def dijkstra(start):
    q = [(0, start)] # 초기화
    while q:
        time, node = heapq.heappop(q)
        if node not in dist:
            dist[node] = time
            for v, w in graph[node]:
                alt = time + w
                heapq.heappush(q, (alt, v))

dijkstra(start)
for i in range(1, V + 1):
    if i not in dist:
        print('INF')
    else:
        print(dist[i])