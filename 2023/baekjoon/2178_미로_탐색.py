# (1, 1) to (n, m) 까지의 최소 칸의 수
# -> (n, m) to (1, 1)
from collections import deque
n, m = map(int, input().split())
# 1: 이동 가능, 0: 이동 불가
board = [
    list(map(int, input()))
    for _ in range(n)
]

ret = 0
visited = [
    [0] * (m)
    for _ in range(n)
]

nx = [0, 1, 0, -1]
ny = [1, 0, -1, 0]

# dfs
def bfs(x, y):
    # 1. 선언
    q = deque()
    # 2. 초기화
    q.append((x, y))
    visited[x][y] = 0
    # 3. 반복
    while q:
        x, y = q.popleft()
        # 사방 확인
        for i in range(4):
            dx = x + nx[i]
            dy = y + ny[i]

            # 범위 확인
            if 0 <= dx < n and 0 <= dy < m and visited[dx][dy] == 0:
                # 범위 내에 있고, 방문하지 않았지만, 갈 수 있다면
                if board[dx][dy] == 1:
                    visited[dx][dy] = visited[x][y] + 1
                    q.append((dx, dy))
                elif board[dx][dy] == 0:
                    visited[dx][dy] = 0


# main
bfs(n-1, m-1)
print(visited[0][0] + 1)