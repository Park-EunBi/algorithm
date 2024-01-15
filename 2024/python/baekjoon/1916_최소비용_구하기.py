import sys
from collections import defaultdict
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = defaultdict(list)
dist = defaultdict(int)

for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append([b, w])

start, end = map(int, input().split())

def dijkstra(start):
    q = [(0, start)] # 초기화
    while q:
        time, node = heapq.heappop(q)
        if node not in dist:
            dist[node] = time
            for b, w in graph[node]:
                alt = w + time
                heapq.heappush(q, [alt, b])

dijkstra(start)
print(dist[end])