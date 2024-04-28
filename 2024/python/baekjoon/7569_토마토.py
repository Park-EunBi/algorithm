# 0: 안익음, 1: 익음, -1: 없음
import sys
from collections import deque
input = sys.stdin.readline

def in_range(z, x, y):
    if x < 0 or x >= n or y < 0 or y >= m or z < 0 or z >= h:
        return False
    return True

def bfs():
    dzs = [-1, 1, 0, 0, 0, 0]
    dxs = [0, 0, 0, 0, -1, 1]
    dys = [0, 0, 1, -1, 0, 0]

    while q:
        z, x, y = q.popleft()
        for dz, dx, dy in zip(dzs, dxs, dys):
            nz, nx, ny = z + dz, x + dx, y + dy
            if in_range(nz, nx, ny) and not visited[nz][nx][ny]:
                if not board[nz][nx][ny]: # 안익었으면
                    q.append((nz, nx, ny))
                    visited[nz][nx][ny] = visited[z][x][y] + 1


    # (토마토가 없는 곳의 수) == (방문하지 않은 곳) -> 모든 토마토가 익음
    # 방문하지 않은 곳 세기
    not_vi = sum([
        1
        for z in range(h)
        for x in range(n)
        for y in range(m)
        if not visited[z][x][y]
    ])

    if no_to == not_vi:
        return visited[z][x][y] - 1
    else: # 모든 토마토가 익지 못함
        return -1

m, n, h = map(int, input().split())
board = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

# 익은 토마토 좌표
q = deque() # z, x, y
visited = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]
no_to = 0 # 토마토가 없는 곳 세기

for z in range(h):
    for x in range(n):
        for y in range(m):
            if board[z][x][y] == 1:
                # 큐에 초깃값 삽입, 방문처리
                q.append((z, x, y))
                visited[z][x][y] = 1
            elif board[z][x][y] == -1:
                no_to += 1

# main
if not len(q):
    print(-1)
    exit(0)

print(bfs())