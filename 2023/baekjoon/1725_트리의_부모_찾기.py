import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())

# 부모 저장
parent = [0] * (n + 1)

# 양방향 연결 정보 저장
graph = [[] for _ in range(n + 1)]

# 양방향 그래프 생성
for _ in range(n-1):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)

# 부모 노드 탐색
def dfs(root):
    # 현재 노드와 연결된 노드 확인
    for n in graph[root]:
        # 연결된 부모가 없다면
        if not parent[n]:
            # 현재 노드를 연결된 노드의 부모 노드로 설정
            parent[n] = root
            dfs(n)

dfs(1)
for i in range(2, n + 1):
    print(parent[i])