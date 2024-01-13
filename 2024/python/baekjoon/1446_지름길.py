import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # 거리, 현재 노드
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        # 최소 비용 체크
        if dist > distance[now]: # 최소 비용 아님
            continue

        # 지름길 일 때 -> 다익스트라 표 갱신
        for i in graph[now]:
            cost = dist + i[1] # 거리 갱신
            if cost < distance[i[0]]: # 최소 거리라면
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

n, d = map(int, input().split())
graph = [
    []
    for _ in range(d + 1)
]
distance = [INF] * (d + 1)

# 거리 초기화
for i in range(d):
    graph[i].append((i+1, 1))

# 지름길 기록
for _ in range(n):
    s, e, l = map(int, input().split())
    if e > d: # 가야할 길 넘어설 때
        continue
    graph[s].append((e, l))

dijkstra(0)
print(distance[d])