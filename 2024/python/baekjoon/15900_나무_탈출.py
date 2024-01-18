import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10 ** 5)
sys.setrecursionlimit(600000)

n = int(input())
graph = [
    []
    for _ in range(n + 1)
]
dist = [0] * (n + 1)
visited = [0] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 루트 ~ 각 리프노드 까지의 거리 짝 - No, 홀 - Yes
# 리프노드 - 인접리스트의 개수가 1개 인 것

def dfs(root):
    visited[root] = 1
    for g in graph[root]:
        if not visited[g]:
            dist[g]  = dist[root] + 1
            dfs(g)

dfs(1)

cnt = 0
# 루트 ~ 리프노드 거리
for i in range(2, n + 1):
    if len(graph[i]) == 1:
        cnt += dist[i]

print('No') if cnt % 2 == 0 else print('Yes')