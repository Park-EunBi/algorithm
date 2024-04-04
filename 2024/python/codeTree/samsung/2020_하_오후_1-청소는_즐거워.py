n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

# 시작 위치 설정
curr_x, curr_y = n // 2, n // 2
move_dir, move_num = 0, 1

ans = 0

dust_ratio = [
    [
        [0, 0, 2, 0, 0],
        [0, 10, 7, 1, 0],
        [5, 0, 0, 0, 0],
        [0, 10, 7, 1, 0],
        [0, 0, 2, 0, 0],
    ],
    [
        [0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [2, 7, 0, 7, 2],
        [0, 10, 0, 10, 0],
        [0, 0, 5, 0, 0],
    ],
    [
        [0, 0, 2, 0, 0],
        [0, 1, 7, 10, 0],
        [0, 0, 0, 0, 5],
        [0, 1, 7, 10, 0],
        [0, 0, 2, 0, 0],
    ],
    [
        [0, 0, 5, 0, 0],
        [0, 10, 0, 10, 0],
        [2, 7, 0, 7, 2],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
    ]
]


def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    return True


# 먼지 추가
def add_dust(x, y, dust):
    global ans

    # 격자 범위를 벗어나면 답에 더하기
    if not in_range(x, y):
        ans += dust
    else:
        board[x][y] += dust


def move():
    global curr_x, curr_y

    # 왼, 아, 오, 위
    dxs, dys = [0, 1, 0, -1], [-1, 0, 1, 0]

    curr_x, curr_y = curr_x + dxs[move_dir], curr_y + dys[move_dir]

    # 각 위치에 먼지 더하기
    added_dust = 0  # 총 이동한 먼지
    for i in range(5):
        for j in range(5):
            dust = board[curr_x][curr_y] * dust_ratio[move_dir][i][j] // 100
            # ✨공부할 부분
            # dust_ratio의 (0, 0) 부터 더해줘야 함
            # 현재 위치를 (0, 0)으로 이동 시키고 (-2, -2)
            # range(5)를 돌며 모든 값을 더해준다
            add_dust(curr_x + i - 2, curr_y + j - 2, dust)

            added_dust += dust

    # a% 자리
    # 내 위치에서 한 칸 앞으로 이동한 자리 (move_dir 방향으로)
    add_dust(curr_x + dxs[move_dir], curr_y + dys[move_dir], board[curr_x][curr_y] - added_dust)


# (0, 0) 확인
def end():
    if curr_x == 0 and curr_y == 0:
        return True
    return False


# main
while not end():
    # move_num 만큼 이동
    for _ in range(move_num):
        move()

        # (0, 0)에 도착하면 종료
        if end():
            break

    # 이동 후 - 회오리 돌리기
    move_dir = (move_dir + 1) % 4
    if move_dir == 0 or move_dir == 2:
        move_num += 1

print(ans)



'''
# 내 풀이 - 틀림
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
'''