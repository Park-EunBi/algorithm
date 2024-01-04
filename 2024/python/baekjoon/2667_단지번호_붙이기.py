# 단지 수, 집의 개수 출력
n = int(input())
board = [
    list(map(int, input()))
    for _ in range(n)
]

houses = []
cnt = 0

def dfs(x, y):
    global cnt
    # 영역 확인
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if board[x][y] == 1:
        board[x][y] = 0
        cnt += 1
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True
    return False

# main
for i in range(n):
    for j in range(n):
        if dfs(i, j):
            houses.append(cnt)
            cnt = 0

houses.sort()
print(len(houses))
for h in houses:
    print(h)