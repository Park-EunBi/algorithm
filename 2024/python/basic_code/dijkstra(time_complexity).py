import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

graph = [
    []
    for _ in range(n + 1)
]

dist = [INF] * (n + 1)
# prev_node = [[0] * (n + 1)]

for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        time, node = heapq.heappop(q)
        # 이미 처리된 적 있는 노드
        if dist[node] < time:
            continue
        for b, w in graph[node]:
            cost = time + w
            if cost < dist[b]:
                # prev_node[b] = node
                dist[b] = cost
                heapq.heappush(q, (cost, b))

dijkstra(start)

for i in range(1, n + 1):
    if dist[i] == INF:
        print('INFINITY')
    else:
        print(dist[i])

'''
end = 3
path = [end]
now = end
while now != start:
    now = prev_node[now]
    path.append(now)
path.reverse()

print(*path)
'''