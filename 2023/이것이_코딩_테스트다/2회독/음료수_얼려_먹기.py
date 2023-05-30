n, m = map(int, input().split())
ice = []
for _ in range(n):
    ice.append(list(map(int, input())))

# 모든 노드를 방문하며
# 0이면 상하좌우 DFS_BFS, return True
# 1이면 return False

def dfs(x, y):
    # 범위를 넘어갔을 경우
    # n : x와 관련, m: y와 관련 주의
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    # 0일 경우
    if ice[x][y] == 0:
        # 방문처리
        ice[x][y] = 1
        # 상 하 좌 우 탐색
        dfs(x, y-1)
        dfs(x, y+1)
        dfs(x-1, y)
        dfs(x+1, y)
        return True
    # 1일 경우
    else:
        return False

# 모든 노드 방문
res = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            res += 1

print(res)

'''
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
'''