from collections import deque
n, m, v = map(int, input().split())
board = [
    []
    for _ in range(n + 1)
]

for _ in range(m):
    a, b = map(int, input().split())
    board[a].append(b)
    board[b].append(a)

for b in board:
    b.sort()

# dfs
def dfs(num):
    visited[num] = True
    print(num, end = ' ')
    for i in board[num]:
        if not visited[i]:
            dfs(i)
# bfs
def bfs(num):
    q = deque()
    q.append(num)
    visited[num] = True

    while q:
        c = q.popleft()
        print(c, end = ' ')
        for i in board[c]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

# main
visited = [False] * (n + 1)
dfs(v)
print()
visited = [False] * (n + 1)
bfs(v)