import sys
sys.stdin = open("input.txt", "rt")

ice = []
n, m = map(int, input().split())
for _ in range(n):
    ice.append(list(map(int,input())))

# dfs
def dfs(x, y):
    # 재귀호출 시 주어진 범위를 넘어갈 수 있기에
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 0이라면 1으로 변경하고 재귀호출
    # 상하좌우 방문
    if ice[x][y] == 0:
        ice[x][y] = 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

# 실행부
res = 0
# 모든 노드 방문하며 True 반환하면 결과 += 1
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            res += 1
print(res)


'''
# input example 
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

result : 8
'''