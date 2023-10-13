# 모든 지점에서 목표지점까지 거리 구하기
# => 목표지점에서 모든 지점까지의 거리를 구하면 된다

from collections import deque
n, m = map(int, input().split())
board = [
    # 0: 못감, 1: 땅, 2: 목표
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [-1] * (m)
    for _ in range(n)
]

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

# 최단거리 -> bfs

def bfs(x, y):
    # q, falg 등 선언
    q = deque()
    # 초기화
    q.append((x, y))
    visited[x][y] = 0
    # 반복
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y

            # 범위 내에 있고 방문한 적 없으면
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
                if board[nx][ny] == 0: # 못감
                    visited[nx][ny] = 0
                elif board[nx][ny] == 1: # 길
                    visited[nx][ny] = visited[x][y] + 1 # 길이 세기
                    q.append((nx, ny))


# bfs 실행
for i in range(n):
    for j in range(m):
        if board[i][j] == 2 and visited[i][j] == -1:
            bfs(i, j)

# 출력
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            print(0, end=' ')
        else:
            print(visited[i][j], end=' ')
    print()