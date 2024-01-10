import sys
sys.setrecursionlimit(10 ** 6)

# 안전 영역의 최대 개수 구하기
n = int(input())
board = [
    list(map(int, input().split()))
    for _ in range(n)
]

maximum = -1
for b in board:
    maximum = max(max(b), maximum)

ret = []
cnt = 0
def dfs(x, y, r):
    # 범위 확인
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    # dfs
    if board[x][y] > r and visited[x][y] == 0: # 비의 양 보다 높은 곳이고 방문하지 않았다면
        visited[x][y] = 1
        dfs(x + 1, y, r)
        dfs(x - 1, y, r)
        dfs(x, y + 1, r)
        dfs(x, y - 1, r)
        return True
    # visited[x][y] = 1
    return False

# main
for rain in range(maximum + 1):
    visited = [
        [0] * n
        for _ in range(n)
    ]
    for a in range(n):
        for b in range(n):
            if dfs(a, b, rain):
                cnt += 1
    ret.append(cnt)
    cnt = 0

print(max(ret))