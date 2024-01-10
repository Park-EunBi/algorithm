import sys
import copy
sys.setrecursionlimit(10**6)
# 적록색약: R == G, B
n = int(input())
color_board = [
    list(input())
    for _ in range(n)
]

# 객체의 참조를 끊어야 함
color_weak_board = copy.deepcopy(color_board)
for board in color_weak_board:
    for i, b in enumerate(board):
        if b == 'G':
            board[i] = 'R'

# print('일반: ', *color_board)
# print('색약: ', *color_weak_board)

def dfs(x, y, c, b):
    # 종료 조건 설정
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    # 탐색
    if b[x][y] == c:
        b[x][y] = 0 # 방문처리
        dfs(x + 1, y, c, b)
        dfs(x - 1, y, c, b)
        dfs(x, y + 1, c, b)
        dfs(x, y - 1, c, b)
        return True
    return False

# main
color_weak = 0
not_color_weak = 0
for color in ('R', 'G', 'B'):
    for x in range(n):
        for y in range(n):
            if dfs(x, y, color, color_board):
                not_color_weak += 1

            if dfs(x, y, color, color_weak_board):
                color_weak += 1

print(not_color_weak, color_weak)