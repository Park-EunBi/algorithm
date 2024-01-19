from collections import deque
import sys
input = sys.stdin.readline

r, c = map(int, input().split())
board = [
    list(input().strip())
    for _ in range(r)
]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
fire = [[0] * c for _ in range(r)]
ji = [[0] * c for _ in range(r)]

f_q = deque()
j_q = deque()

for i in range(r):
    for j in range(c):
        if board[i][j] == 'F':
            f_q.append((i, j))
            fire[i][j] = 1
        elif board[i][j] == 'J':
            j_q.append((i, j))
            ji[i][j] = 1

def fire_bfs():
    while f_q:
        x, y = f_q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if board[nx][ny] == '.' and fire[nx][ny] == 0:
                    fire[nx][ny] = fire[x][y] + 1
                    f_q.append((nx, ny))

def ji_bfs():
    while j_q:
        x, y = j_q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 경로 이탈
            if not (0 <= nx < r and 0 <= ny < c):
                print(ji[x][y])
                return

            # 지훈이가 지나온 길이거나 벽이라면 contine
            if ji[nx][ny] or board[nx][ny] == '#':
                continue

            # 불이 확산되었고, 지훈이가 해당 위치로 이동할 시간보다 불이 먼저 왔다면
            if fire[nx][ny] and ji[x][y] + 1 >= fire[nx][ny]:
                continue

            # 최단 경로 갱신
            ji[nx][ny] = ji[x][y] + 1
            j_q.append((nx, ny))

    print('IMPOSSIBLE')
    return

fire_bfs()
ji_bfs()