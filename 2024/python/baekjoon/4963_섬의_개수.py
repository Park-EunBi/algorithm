import sys
sys.setrecursionlimit(10**6)
while 1:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    board = [
        list(map(int, input().split()))
        for _ in range(h)
    ]

    cnt = 0
    def dfs(x, y):
        if x < 0 or x >= h or y < 0 or y >= w:
            return False

        if board[x][y] == 1:
            board[x][y] = 0
            # 대각선도 이동 가능
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
            dfs(x + 1, y + 1)
            dfs(x - 1, y - 1)
            dfs(x + 1, y - 1)
            dfs(x - 1, y + 1)
            return True
        return False

    for i in range(h):
        for j in range(w):
            if dfs(i, j):
                cnt += 1

    print(cnt)

