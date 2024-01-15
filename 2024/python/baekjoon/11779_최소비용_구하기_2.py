import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = [
    []
    for _ in range(n + 1)
]

dist = [INF] * (n + 1)
prev_node = [0] * (n + 1)

for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))

start, end = map(int, input().split())

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
                prev_node[b] = node
                dist[b] = cost
                heapq.heappush(q, (cost, b))

dijkstra(start)
print(dist[end])

path = [end]
now = end
while now != start:
    now = prev_node[now]
    path.append(now)
path.reverse()

print(len(path))
print(*path)
