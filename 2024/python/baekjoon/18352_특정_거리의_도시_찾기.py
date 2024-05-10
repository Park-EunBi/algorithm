import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split())

board = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    board[a].append(b)

ans = []
def bfs():
    while q:
        x = q.popleft()
        if visited[x]-1 == k:
            ans.append(x)

        for nx in board[x]:
            if not visited[nx]:
                visited[nx] = visited[x] + 1
                q.append(nx)


# main
q = deque()
q.append(x)
visited[x] = 1
bfs()

if not len(ans):
    print(-1)
    exit(0)

ans.sort()
for a in ans:
    print(a)