import sys
n = int(input())
board = [
    list(map(int, input()))
    for _ in range(n)
]

ret = []
cnt = 0

def dfs(x, y):
    global cnt
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if board[x][y] == 1:
        cnt += 1
        board[x][y] = 0
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y -1)
        return True
    return False

for i in range(n):
    for j in range(n):
        if dfs(i, j):
            ret.append(cnt)
            cnt = 0
ret.sort()
print(len(ret))
for r in ret:
    print(r)