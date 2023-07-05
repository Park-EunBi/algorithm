# 1 ~ N 번까지의 도시, M개의 단방향 도로
# x 도시로부터 출발하여 도달할 수 있는 모든 도시 중
# 최단 거리가 정확히 k인 모든 도시의 번호 출력
# 한 줄에 하나씩 오름차순으로, 없다면 -1 출력
# 모든 간선의 길이가 동일할 때 BFS 사용 가능

from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 최단 거리 초기화 
distance = [-1] * (n + 1)
distance[x] = 0 # 자기 자신까지의 거리는 0

# BFS
q = deque([x])
while q:
    now = q.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시 확인
    for next_node in graph[now]:
        if distance[next_node] == -1:
            # 최단 거리 갱신
            distance[next_node] = distance[now] + 1
            q.append(next_node)

# 최단 거리가 k인 모든 도시의 번호 출력 (오름차순)
check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

# 최단 거리가 k인 도시가 없다면 -1 출력
if check == False:
    print(-1)


'''
<testCase1>
4 4 2 1
1 2
1 3
2 3
2 4

<answer1>
4

<testCase2>
4 3 2 1
1 2
1 3
1 4

<answer2>
-1

<testCase3>
4 4 1 1
1 2
1 3
2 3
2 4

<answer3>
2
3
'''