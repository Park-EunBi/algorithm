n, r, c = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 상하좌우
dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
move = True # 초깃값 주의

def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    return True

def simulation(x, y):
    global move
    # 1. 현재 값 확인
    now = board[x][y]
    # 2. 이동
    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        if in_range(nx, ny) and now < board[nx][ny]:
            return nx, ny # 모든 영역 탐색하지 않도록 조건 만족하면 바로 return
    move = False
    return x, y


x = r - 1
y = c - 1

while move: # 반복 조건 주의
    print(board[x][y], end=' ')
    x, y = simulation(x, y)
