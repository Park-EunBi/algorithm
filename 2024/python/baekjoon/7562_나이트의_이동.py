from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
dxs, dys = [-1, -2, -2, -1, 1, 2, 2, 1], [-2, -1, 1, 2, 2, 1, -1, -2]

def can_go(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if visited[x][y]:
        return False
    return True

def push(x, y, s):
    # 1. 추가
    q.append((x, y))
    # 2. 방문 처리, 이동 거리 갱신
    visited[x][y] += s

def bfs():
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                push(nx, ny, visited[x][y] + 1)

for _ in range(t):
    ans = 0
    q = deque()
    n = int(input()) # (4 ≤ n ≤ 300)
    visited = [[0 for _ in range(n)] for _ in range(n)]
    board = [[0 for _ in range(n)] for _ in range(n)]
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())

    # main
    q.append((sx, sy))
    visited[sx][sy] = 1
    bfs()
    print(visited[ex][ey] - 1)