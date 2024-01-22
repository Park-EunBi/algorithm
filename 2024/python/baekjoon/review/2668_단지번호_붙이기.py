n = int(input())
board = [
    list(map(int, input()))
    for _ in range(n)
]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
cnt = 0
ret = []

def dfs(x, y):
    global cnt
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if board[x][y] == 1:
        board[x][y] = 0
        cnt += 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            dfs(nx, ny)
        return True
    return False

for i in range(n):
    for j in range(n):
        if dfs(i, j):
            ret.append(cnt)
            cnt = 0

print(len(ret))
for r in sorted(ret):
    print(r)