# 1: 그림, 0: 빈 곳
from collections import deque
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]

def canGo(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if visited[x][y] or not board[x][y]:
        return False
    return True

def bfs():
    cnt = 1
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if canGo(nx, ny):
                q.append((nx, ny))
                visited[nx][ny] = 1
                cnt += 1
    return cnt

ans = [0]
for i in range(n):
    for j in range(m): #### n 아님
        if canGo(i, j):
            q = deque()
            q.append((i, j))
            visited[i][j] = 1
            ans.append(bfs())

ans.sort(reverse = True)
print(len(ans)-1)
print(ans[0])