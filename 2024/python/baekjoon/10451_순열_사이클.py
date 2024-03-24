t = int(input())

def dfs(num):
    visited[num] = 1

    # 인접 노드 판단
    for c in graph[num]:
        if not visited[c]:
            dfs(c)

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    graph = [[] for _ in range(n + 1)]

    for idx, nu in enumerate(nums):
        graph[idx + 1].append(nu)

    visited = [0] * (n + 1)
    cnt = 0
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
            cnt += 1

    print(cnt)