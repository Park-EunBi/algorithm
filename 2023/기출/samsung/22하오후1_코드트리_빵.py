import sys
from collections import deque

INT_MAX = sys.maxsize
EMPTY = (-1, -1)

# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))

# 0: 빈칸, 1: 베이스캠프, 2: 아무도 못감
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 편의점 목록 관리
cvs_list = []
for _ in range(m):
    x, y = tuple(map(int, input().split()))
    cvs_list.append((x-1, y-1))

# 현재 사람들의 위치 관리
people = [EMPTY] * m

# 현재 시간
curr_t = 0

# 상좌우하
dxs = [-1, 0, 0, 1]
dys = [0, -1, 1, 0]

# bfs에 사용
# 1. 최단거리 결과 기록
step = [
    [0] * n
    for _ in range(n)
]

# 2. 방문여부 표시
visited = [
    [False] * n
    for _ in range(n)
]

# (x, y)가 격자내에 있는 좌표인지
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

# (x, y)로 이동 가능 판단
def can_go(x, y):
    # 범위를 벗어나지 않으면서, 방문했던 적이 없으면서, 이동가능한 곳
    return in_range(x, y) and not visited[x][y] and grid[x][y] != 2

# bfs
# 시작점으로부터 최단거리 결과는 step 배열에 기록
def bfs(start_pos):
    # 초기화
    for i in range(n):
        for j in range(n):
            visited[i][j] = False
            step[i][j] = 0

    # 초기 위치 삽입
    q = deque()
    q.append(start_pos)
    sx, sy = start_pos
    visited[sx][sy] = True
    step[sx][sy] = 0

    # bfs
    while q:
        # 가장 앞의 원소 선택
        x, y = q.popleft()

        # 인접한 칸 중 아직 방문하지 않은 칸은 큐에 넣기
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            # 갈 수 있다면 진행
            if can_go(nx, ny):
                visited[nx][ny] = True
                step[nx][ny] = step[x][y] + 1
                q.append((nx, ny))

# 시뮬 진행
def simulation():
    # step1. 격자에 있다면 편의점 방향으로 1칸 이동
    for i in range(m):
        # 격자 밖에 있거나 편의점에 도착했다면 패스
        if people[i] == EMPTY or people[i] == cvs_list[i]:
            continue

        # 최단거리가 되기 위한 다음 위치를 구하기 위해서는
        # 편위점 위치를 시작으로 현재 위치까지 오는 최단 거리 구해야 한다
        bfs(cvs_list[i])

        px, py = people[i]
        # 현재 위치에서 상좌우하 중 최단 거리 값이 가장 작은 곳을 고르면
        # 그 곳으로 이동하는 것이 최단거리 대로 이동하는 것
        min_dist = INT_MAX
        min_x, min_y = -1, -1
        for dx, dy in zip(dxs, dys):
            nx, ny = px + dx, py +dy
            if in_range(nx, ny) and visited[nx][ny] and min_dist > step[nx][ny]:
                min_dist = step[nx][ny]
                min_x, min_y = nx, ny

        # 우선순위가 가장 높은 위치로 한 칸 이동
        people[i] = (min_x, min_y)

    # step2. 편의점 도착 -> 2로 변경
    for i in range(m):
        if people[i] == cvs_list[i]:
            px, py = people[i]
            grid[px][py] = 2

    # step3. curr_t <= m을 만족하면 t 번 사람 베이스캠프로 이동
    if curr_t > m:
        return

    # step 3-1. 편의점으로부터 가장 가까운 베이스캠프 선택
    #          편의점을 시작으로 하는 bfs 진행
    bfs(cvs_list[curr_t - 1])

    # step 3-2. 편의점에서 가장 가까운 베이스캠프 선택
    #           i, j 순서로 돌아가기에 행 -> 열 우선순위대로 선택
    min_dist = INT_MAX
    min_x, min_y = -1, -1
    for i in range(n):
        for j in range(n):
            # 거리가 가장 가까운 위치 선택
            if visited[i][j] and grid[i][j] == 1 and min_dist > step[i][j]:
                min_dist = step[i][j]
                min_x, min_y = i, j

    # 우선순위가 가장 높은 베이스캠프로 이동
    people[curr_t -1] = (min_x, min_y)
    # 이동 불가 처리
    grid[min_x][min_y] = 2

# 전부 도착 확인
def end():
    for i in range(m):
        # 한 명이라도 도착하지 못했다면
        if people[i] != cvs_list[i]:
            return False
    # 모두 도착
    return True

while 1:
    curr_t += 1
    simulation()
    if end():
        break

print(curr_t)