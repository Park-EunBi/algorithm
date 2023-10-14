# 목표지점 to 모든 지점
from collections import deque

n, m = map(int, input().split()) # 세로, 가로

# 0: 못 감, 1: 감, 2: 목표
board = [
    list(map(int, input().split()))
    for _ in range(n)
]

# -1: 미방문 0 ~ : 방문 횟수
visited = [
    [-1] * m
    for _ in range(n)
]

nx, ny = [0, 1, 0, -1], [1, 0, -1, 0]

# bfs
def bfs(x, y):
    # 1. 선언
    q = deque()
    # 2. 초기화
    q.append((x, y))
    visited[x][y] = 0
    # 3. 반복
    while q:
        # 뽑기
        x, y = q.popleft()

        # 뽑은 값 주변 확인
        for i in range(4):
            # 위치 idx 갱신
            dx = x + nx[i]
            dy = y + ny[i]

            # 범위 확인
            if 0 <= dx < n and 0 <= dy < m and visited[dx][dy] == -1:
                # 지도 확인
                if board[dx][dy] == 0: # 못 감
                    visited[dx][dy] = 0
                elif board[dx][dy] == 1: # 갈 수 있음
                    visited[dx][dy] = visited[x][y] + 1 # 기존 값 += 1
                    # q 에 추가
                    q.append((dx, dy))
# main
for i in range(n):
    for j in range(m):
        if visited[i][j] == -1 and board[i][j] == 2:
            bfs(i, j)

# 출력
# 틀린 출력
# for v in visited:
#     print(*v)

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            print(0, end=' ') # 이 처리 안해줌 틀림
        else:
            print(visited[i][j], end=' ')
    print()