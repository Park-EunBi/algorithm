m, n = map(int, input().split())
board = [0] * (n + 1)
ret = []
for i in range(2, n + 1):
    if board[i] == 0:
        board[i] = 1
        if i >= m:
            ret.append(i)
        for j in range(i, n + 1, i):
            if board[j] == 0:
                board[j] = 1

for r in ret:
    print(r)