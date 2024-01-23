import sys
sys.setrecursionlimit(10**7)
input= sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n + 1)
cnt = 0
def dfs(node):
    visited[node] = 1
    for i in graph[node]:
        if not visited[i]:
            dfs(i)

for i in range(1, n + 1):
    if not visited[i]:
        cnt += 1
        dfs(i)
print(cnt)