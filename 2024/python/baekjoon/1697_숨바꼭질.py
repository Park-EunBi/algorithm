# 최단거리
from collections import deque
n, k = map(int, input().split())
visited = [0] * (1000000 + 1)

def bfs(start):
    q = deque([start])
    while q:
        c = q.popleft()

        if c == k:
            return visited[k]

        for i in (c-1, c+1, c*2):
            if 0 <= i <= 1000000 and not visited[i]:
                visited[i] = visited[c] + 1
                q.append(i)

print(bfs(n))