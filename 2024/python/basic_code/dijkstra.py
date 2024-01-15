import heapq
from collections import defaultdict
import sys
input = sys.stdin.readline

# 입력
n, m = map(int, input().split())
start = int(input()) # 시작 노드

# 그래프 생성
graph = defaultdict(list)
dist = defaultdict(int)
prev_node = [0] * (n + 1) # 경로 확인시 사용
for _ in range(m):
    u, v, w = map(int, input().split()) # 시작 노드, 도착 노드, 가중치
    graph[u].append((v, w))

# 다익스트라
def dijkstra(start):
    # 큐 변수 : (소요시간, 정점)
    q = [(0, start)] # 초기화

    while q:
        # 최단 거리가 가장 짧은 노드 꺼내기
        time, node = heapq.heappop(q)
        # 처리된 적 없는 노드라면
        if node not in dist:
            dist[node] = time
            # 현재 노드의 인접 노드들 확인
            for v, w in graph[node]:
                prev_node[v] = node # 경로 입력
                # 거리 갱신
                alt = time + w
                heapq.heappush(q, (alt, v))

dijkstra(start)
for i in range(1, n + 1):
    if i not in dist:
        print('INFINITY')
    else:
        print(dist[i])

print(prev_node)

'''
# 경로 구하기 
end = 6
path = [end]
now = end
while now != start:
    now = prev_node[now]
    path.append(now)
print(path.reverse)
'''

'''
# testcase
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2

# ans
0
2
3
1
2
4
'''