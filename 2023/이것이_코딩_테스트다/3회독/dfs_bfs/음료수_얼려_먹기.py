# 0: 구멍, 1: 칸막이
# 생성되는 아이스크림의 개수

n, m = map(int, input().split())
ices = []
for _ in range(n):
    ices.append(list(map(int, input())))

ret = 0
def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if ices[x][y] == 0:
        ices[x][y] = 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False

for i in range(n):
    for j in range(m):
        if dfs(i, j):
            ret += 1

print(ret)

'''
<testCase1>
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

<answer1>
8
'''