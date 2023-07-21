# 1 ~ K 번까지의 바이러스 (낮은 번호부터 증식)
# s 초 이후 (x, y)에 존재하는 바이러스의 종류 출력

from collections import deque

n, k = map(int, input().split())

graph = [] # 전체 지도 정보 저장
data = [] # 바이러스 정보 저장

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))

data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, input().split())

# 퍼져 나갈 수 있는 4가지 위치
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# bfs
while q:
    virus, s, x, y = q.popleft()
    if s == target_s:
        break

# 현재 노드에서 상하좌우 위치 확인
for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= nx and nx < n and 0 <= ny and ny < n:
        if graph[nx][ny] == 0:
            graph[nx][ny] = virus
            q.append((virus, s + 1, nx, ny))

print(graph[target_x -1][target_y -1])

'''
<testCase1>
3 3
1 0 2
0 0 0
3 0 0
2 3 2

<answer1>
3

<testCase2>
3 3
1 0 2
0 0 0
3 0 0
1 2 2

<answer2>
0
'''