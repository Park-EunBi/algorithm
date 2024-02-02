import sys
from collections import deque 
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
board = [[] for _ in range(n + 1)]
boardR = [[] for _ in range(n + 1)] # 역방향 그래프 
for _ in range(m):
    a, b = map(int, input().split())
    board[a].append(b)
    boardR[b].append(a)
s, t = map(int, input().split())

def dfs(now, adj, visited):
    if visited[now]:
        return 
    visited[now] = 1
    for a in adj[now]:
        dfs(a, adj, visited)
    return 

fromS = [0] * (n + 1)
fromS[t] = 1 # 도착지에 도착하면 멈추도록 
dfs(s, board, fromS)

fromT = [0] * (n + 1)
fromT[s] = 1
dfs(t, board, fromT)

toS = [0] * (n + 1)
dfs(s, boardR, toS)

toT = [0] * (n + 1)
dfs(t, boardR, toT)

count = 0
for i in range(1, n + 1):
    if fromS[i] and fromT[i] and toS[i] and toT[i]:
        count += 1
print(count -2)