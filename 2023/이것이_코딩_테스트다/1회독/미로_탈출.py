import sys
sys.stdin = open("input.txt", "rt")
from collections import deque
# 출발 지점: (1, 1), 출구: (n, m)
# 한 번에 한 칸 씩 이동 가능
# 괴물이 있는 부분은 0, 없는 부분은 1
# 움직여야 하는 최소 칸의 개수
# 시작 칸과 마지막 칸을 포함하여 카운트

maze = []
n, m = map(int, input().split())
for _ in range(n):
    maze.append(list(map(int, input())))

# 이동 방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# bfs
def bfs (x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            # 이동
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위를 넘어가거나
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 괴물을 만난 경우
            if maze[nx][ny] == 0:
                continue
            # 길인 경우 1초
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))
    return maze[n-1][m-1]

print(bfs(0, 0))