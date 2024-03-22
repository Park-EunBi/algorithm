# 0: 벽, 1: 길
from collections import deque

def solution(maps):
    dxs, dys = [0, 0, 1, -1], [-1, 1, 0, 0]
    q = deque()

    def in_range(x, y):
        if x < 0 or x >= n or y < 0 or y >= m:
            return False
        return True

    def bfs():
        while q:
            x, y = q.popleft()
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if in_range(nx, ny) and not visited[nx][ny] and maps[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))

    n = len(maps)
    m = len(maps[0])
    visited = [[0] * m for _ in range(n)]

    q.append((0, 0))
    visited[0][0] = 1

    bfs()

    if visited[n - 1][m - 1]:
        return visited[n - 1][m - 1]
    else:
        return -1