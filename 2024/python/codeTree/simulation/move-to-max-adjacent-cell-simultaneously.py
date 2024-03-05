n, m, t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
start = [tuple(map(int, input().split())) for _ in range(m)]
count = [[0 for _ in range(n)] for _ in range(n)]  # 구슬 위치 기록

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

for s in start:
    count[s[0] - 1][s[1] - 1] = 1

def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    return True

# 상하좌우 중 가장 큰 수로 이동
def move(x, y):
    nums = []  # 상하좌우 값 기록
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny):
            nums.append(board[nx][ny])
        else:
            nums.append(0)

    max_idx = nums.index(max(nums))
    x += dxs[max_idx]
    y += dys[max_idx]

    '''
    # 최댓값 갱신 
    max_num = 0
    max_pos = (0, 0)

        if in_range(nx, ny) and board[nx][ny] > max_num:
            max_num = board[nx][ny]
            max_pos = (nx, ny)
    '''
    return x, y

# main
# 구슬의 위치를 기록하는 것이 아니라
# 구슬의 숫자를 기록하고 구슬이 있다면 움직이는 방식으로 작동
for _ in range(t):
    # 1. temp 초기화
    temp = [[0 for _ in range(n)] for _ in range(n)]

    # 2. 구슬 이동
    for i in range(n):
        for j in range(n):
            if count[i][j] == 1:  # 2 이상은 안된다
                x, y = move(i, j)
                temp[x][y] += 1

    # 3. count 변수에 복사
    for i in range(n):
        for j in range(n):
            if temp[i][j] != 1:
                count[i][j] = 0
            else:
                count[i][j] = 1

cnt = sum([
    count[i][j]
    for i in range(n)
    for j in range(n)
])

print(cnt)