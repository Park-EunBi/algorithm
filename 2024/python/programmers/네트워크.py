def dfs(x, visited, n, computers):
    # 1. 방문 처리
    visited[x] = 1
    # 인접 노드 방문
    for i in range(n):
        if computers[x][i] == 1 and not visited[i]:  # x와 i가 연결되어 있고, 아직 방문하지 않았다면
            dfs(i, visited, n, computers)


def solution(n, computers):
    cnt = 0
    visited = [0] * n
    for i in range(n):
        if not visited[i]:  # 아직 방문하지 않은 노드라면
            dfs(i, visited, n, computers)
            cnt += 1  # 새로운 네트워크 발견

    print(cnt)
    return cnt
