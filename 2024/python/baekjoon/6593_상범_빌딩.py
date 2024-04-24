import sys
from collections import deque
input = sys.stdin.readline

dzs = [0, 0, 0, 0, 1, -1]
dxs = [0, 0, 1, -1, 0, 0]
dys = [1, -1, 0, 0, 0, 0]

def in_range(z, x, y):
    if 0 > x or x >= r or 0 > y or y >= c or 0 > z or z >= l:
        return False
    return True

def bfs():
    while q:
        z, x, y = q.popleft()
        for dz, dx, dy in zip(dzs, dxs, dys):
            nz, nx, ny = z + dz, x + dx, y + dy
            if in_range(nz, nx, ny) and not visited[nz][nx][ny]:
                if board[nz][nx][ny] == '.':
                    visited[nz][nx][ny] = visited[z][x][y] + 1
                    q.append((nz, nx, ny))

                if board[nz][nx][ny] == 'E':
                    visited[nz][nx][ny] = visited[z][x][y] + 1
                    return

while 1:
    l, r, c = map(int, input().split())

    if (l, r, c) == (0, 0, 0):
        break

    board = []
    for _ in range(l):
        board.append([list(input().strip()) for _ in range(r)])
        input() #### 입력 값 주의...

    # 입구, 출구 등록
    for i in range(r):
        for j in range(c):
            for k in range(l):
                if board[k][i][j] == 'S':
                    sx, sy, sz = i, j, k
                elif board[k][i][j] == 'E':
                    ex, ey, ez = i, j, k

    q = deque()
    q.append((sz, sx, sy))
    visited = [[[0 for _ in range(c)] for _ in range(r)] for _ in range(l)]
    visited[sz][sx][sy] = 1
    bfs()

    if visited[ez][ex][ey]:
        print(f'Escaped in {visited[ez][ex][ey] - 1} minute(s).')
    else:
        print('Trapped!')