n, m, t = map(int, input().split())
balls = [list(input().split()) for _ in range(m)]
count = [[0 for _ in range(n)] for _ in range(n)]

dxs, dys = [-1, 0, 0, 1], [0, 1, -1, 0]
direction = {
    'U': 0,
    'R': 1,
    'L': 2,
    'D': 3
}

# balls, count 전처리
for b in balls:
    b[0] = int(b[0]) - 1
    b[1] = int(b[1]) - 1
    b[2] = direction[b[2]]
    b[3] = int(b[3])
    count[b[0]][b[1]] += 1


###### fun
def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    return True


# b에 입력된 방향대로 이동
def move(b):
    x, y, d, w = b
    nx, ny = x + dxs[d], y + dys[d]
    if in_range(nx, ny):
        return (nx, ny, d, w)
    else:
        return (x, y, 3 - d, w)


def simulation():
    global balls, count
    # 1. 구슬 이동
    temp_balls = []
    for b in balls:
        temp_balls.append(move(b))
    balls = temp_balls

    # 2. count update
    temp_count = [[0 for _ in range(n)] for _ in range(n)]
    for b in balls:
        temp_count[b[0]][b[1]] += 1
    count = temp_count

    # 3. 충돌 처리 - 무게처리(방향 - 덮어쓰기, 무게 - 더하기), 제거
    # count 돌다가 2 이상인 값 만나면
    # balls 에서 x, y 같은 거 찾아서 wight, direction 갱신
    for i in range(n):
        for j in range(n):
            # 충돌 감지
            nw = 0
            nd = -1
            max_idx = -1
            if count[i][j] > 1:
                # 누군지 찾기
                for idx, b in enumerate(balls):
                    if b[0] == i and b[1] == j:
                        nw += b[3]
                        nd = b[2]
                        max_idx = idx
                        # 지우기
                        balls[idx] = (-1, -1, -1, -1)

                count[i][j] = 1
                balls[max_idx] = (i, j, nd, nw)

    temp_balls = []
    for idx, b in enumerate(balls):
        if b == (-1, -1, -1, -1):
            continue
        else:
            temp_balls.append(b)

    balls = temp_balls


###### main
for _ in range(t):
    simulation()

cnt = sum([
    count[i][j]
    for i in range(n)
    for j in range(n)
])

weight = max([
    balls[i][3]
    for i in range(len(balls))
])

print(cnt, weight)

'''
sol_2
EMPTY = (0, 0, 0)

# 변수 선언 및 입력:
n, m, t = tuple(map(int, input().split()))
grid = [
    [EMPTY for _ in range(n)]
    for _ in range(n)
]
next_grid = [
    [EMPTY for _ in range(n)]
    for _ in range(n)
]


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


def next_pos(x, y, move_dir):
    # 방향 전환을 쉽게 하기 위해 
    # dx, dy 테크닉에서 0<->3, 1<->2가
    # 서로 반대 방향이 되도록 정의합니다.
    dxs, dys = [-1, 0, 0, 1], [0, 1, -1, 0]

    nx, ny = x + dxs[move_dir], y + dys[move_dir]

    # 벽에 부딪히게 된다면, 방향만 전환해줍니다.
    if not in_range(nx, ny):
        move_dir = 3 - move_dir
    # 그렇지 않다면, 한 칸 전진합니다.
    else:
        x, y = nx, ny

    return (x, y, move_dir)


# (x, y) 위치에 새로운 구슬이 들어왔을 때 갱신을 진행합니다.
def update(x, y, new_marble):
    # 기존 구슬 정보입니다.
    num, weight, move_dir = next_grid[x][y]

    # 새롭게 들어온 구슬 정보입니다.
    new_num, new_weight, new_dir = new_marble

    # 새로 들어온 구슬이 더 우선순위가 높다면
    # 번호와 방향은 새로운 구슬을 따르게 됩니다.
    if new_num > num: 
        next_grid[x][y] = (new_num, weight + new_weight, new_dir)
    # 기존 구슬의 우선순위가 더 높다면
    # 무게만 더해집니다.
    else:
        next_grid[x][y] = (num, weight + new_weight, move_dir)


def move(x, y):
    num, weight, move_dir = grid[x][y]

    # Step1. 현재 구슬의 다음 위치와 방향을 구합니다.
    nx, ny, next_dir = next_pos(x, y, move_dir)

    # Step2. 구슬을 옮겨줍니다.
    update(nx, ny, (num, weight, next_dir))


def simulate():
    # Step1. next_grid를 초기화합니다.
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = EMPTY

    # Step2. 각 구슬들을 한 칸씩 움직여줍니다.
    for i in range(n):
        for j in range(n):
            if grid[i][j] != EMPTY:
                move(i, j)

    # Step3. next_grid 값을 grid로 옮겨줍니다.
    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]


def get_marble_num():
    cnt = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] != EMPTY:
                cnt += 1

    return cnt


def get_max_weight():
    max_weight = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] != EMPTY:
                _, weight, _ = grid[i][j]
                max_weight = max(max_weight, weight)

    return max_weight


dir_mapper = {
    "U": 0,
    "R": 1,
    "L": 2,
    "D": 3
}

for i in range(m):
    r, c, d, w = tuple(input().split())
    r, c, w = tuple(map(int, [r, c, w]))
    grid[r - 1][c - 1] = (i + 1, w, dir_mapper[d])

# t초에 걸쳐 시뮬레이션을 진행합니다.
for _ in range(t):
    simulate()

marble_num, max_weight = get_marble_num(), get_max_weight()
print(marble_num, max_weight)
'''