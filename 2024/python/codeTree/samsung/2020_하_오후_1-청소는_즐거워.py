n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
temp = [[0 for _ in range(n)] for _ in range(n)]
clean = {
    0: {
        (-1, 1): 0.01,
        (1, 1): 0.01,
        (-2, 0): 0.02,
        (2, 0): 0.02,
        (-1, 0): 0.07,
        (1, 0): 0.07,
        (0, -2): 0.05,
        (-1, -1): 0.1,
        (1, -1): 0.1},

    1: {
        (-1, -1): 0.01,
        (-1, 1): 0.01,
        (0, -2): 0.02,
        (0, 2): 0.02,
        (0, -1): 0.07,
        (0, 1): 0.07,
        (-2, 0): 0.05,
        (1, -1): 0.1,
        (1, 1): 0.1},

    2: {
        (-1, -1): 0.01,
        (1, -1): 0.01,
        (-2, 0): 0.02,
        (2, 0): 0.02,
        (-1, 0): 0.07,
        (1, 0): 0.07,
        (0, 2): 0.05,
        (-1, 1): 0.1,
        (1, 1): 0.1},

    3: {
        (1, -1): 0.01,
        (1, 1): 0.01,
        (0, -2): 0.02,
        (0, 2): 0.02,
        (0, -1): 0.07,
        (0, 1): 0.07,
        (-2, 0): 0.05,
        (-1, -1): 0.1,
        (-1, 1): 0.1}
}
print('<<init - board>>')
for b in board:
    print(*b)
print()

def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    return True

# 한 라인씩 이동
def move(x, y, delta):
    global d
    # 방향 변경
    d = (d + 1) % 4
    if d == 0 or d == 2:
        delta += 1

    print(f'd: {d}, delta: {delta}')

    for i in range(1, delta + 1):
        x, y = x + dxs[d], y + dys[d]
        #### test 용
        temp[x][y] = '*'
        cleanning(x, y, d)

        print('<<이동 - temp>>')
        for t in temp:
            print(*t)
        print()
        board[x][y] = 0

        print('<<청소 - board>>')
        for b in board:
            print(*b)
        print()

    return x, y, delta

clean_a = {
    0: (0, -1),
    1: (1, 0),
    2: (0, 1),
    3: (-1, 0)
}

def cleanning(x, y, d):
    global ans
    print(f'x:{x}, y:{y}, board[x][y]: {board[x][y]}')
    total = 0 # 다른 곳으로 이동한 먼지 양 세기
    # 1. clean에 저장된 % 만큼 먼지 치워서 더하기
    for dx, dy in clean[d]:
        nx, ny = x + dx, y + dy
        percent = clean[d][(dx, dy)]
        temp = int(board[x][y] * percent)
        total += temp
        if in_range(nx, ny):
            board[nx][ny] += temp
        else:
            print(f'떨어진 먼지: {temp}')
            # print(f'here: {temp}, nx, ny :{nx}, {ny}')
            ans += temp # 떨어진 먼지

        print(f'nx: {nx}, ny:{ny}, percent: {percent}, temp : {temp}')

    # a 구하기
    a = board[x][y] - total

    print(f'a:{a}')
    # print(f'a%:{board[x][y] * 0.01 * a}')

    dx, dy = clean_a[d]
    nx, ny = x + dx, y + dy
    if in_range(nx, ny):
        board[nx][ny] += a
    else:
        print(f'떨어진 먼지: {a}')
        ans += a
        # board[x + dx][y + dy] += a

    print(f'ans: {ans}')

# main
x, y = n//2, n//2
d = 3 # 방향
delta = 0 # 얼마나 움직일지
dxs, dys = [0, 1, 0, -1], [-1, 0, 1, 0]
ans = 0
for _ in range(2 * n - 1):
    # 1. 이동 - 한 라인씩
    x, y, delta = move(x, y, delta)

#####################
# 하드 코딩 있음
#####################

print(f'ans: {ans}')