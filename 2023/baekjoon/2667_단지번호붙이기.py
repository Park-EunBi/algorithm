# dfs
# 1. 단지 수 세기
# 2. 단지 내 집의 개수를 오름차순 출력

# 입력 받기
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(input()))

# 단지 내 집의 수 계산 변수
cnt = 0
# 결과를 담을 리스트
result = []

def dfs(x,y):
    global cnt
    # 예외처리
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    # 1이면 방문
    if int(graph[x][y]) == 1:
        cnt += 1
        # 방문 처리
        graph[x][y] = 0
        dfs(x, y - 1)
        dfs(x, y + 1)
        dfs(x - 1, y)
        dfs(x + 1, y)
        return True
    return False

for i in range(n):
    for j in range(n):
        if dfs(i, j):
            result.append(cnt)
            cnt = 0

result.sort()
print(len(result))
for i in result:
    print(i)


