# 변수 선언 및 입력:
n, m, k, c = tuple(map(int, input().split()))
tree = [[0] * (n + 1)]
for _ in range(n):
    tree.append([0] + list(map(int, input().split())))

add_tree = [
    [0] * (n + 1)
    for _ in range(n + 1)
]
herb = [
    [0] * (n + 1)
    for _ in range(n + 1)
]

ans = 0


def is_out_range(x, y):
    return not (1 <= x and x <= n and 1 <= y and y <= n)


# 1단계 : 인접한 네 개의 칸 중 나무가 있는 칸의 수만큼 나무가 성장합니다.
def step_one():
    dxs, dys = [-1, 0, 1, 0], [0, -1, 0, 1]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if tree[i][j] <= 0:
                continue

            # 나무가 있는 칸의 수(cnt)만큼 나무가 성장합니다.
            cnt = 0
            for dx, dy in zip(dxs, dys):
                nx, ny = i + dx, j + dy
                if is_out_range(nx, ny):
                    continue
                if tree[nx][ny] > 0:
                    cnt += 1

            tree[i][j] += cnt


# 2단계 : 기존에 있었던 나무들은 아무것도 없는 칸에 번식을 진행합니다.
def step_two():
    dxs, dys = [-1, 0, 1, 0], [0, -1, 0, 1]

    # 모든 나무에서 동시에 일어나는 것을 구현하기 위해 하나의 배열을 더 이용합니다.
    # add_tree를 초기화해줍니다.
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            add_tree[i][j] = 0

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if tree[i][j] <= 0:
                continue

            # 해당 나무와 인접한 나무 중 아무도 없는 칸의 개수를 찾습니다.
            cnt = 0
            for dx, dy in zip(dxs, dys):
                nx, ny = i + dx, j + dy
                if is_out_range(nx, ny):
                    continue
                if herb[nx][ny]:
                    continue
                if tree[nx][ny] == 0:
                    cnt += 1

            # 인접한 나무 중 아무도 없는 칸은 cnt로 나눠준 만큼 번식합니다.
            for dx, dy in zip(dxs, dys):
                nx, ny = i + dx, j + dy
                if is_out_range(nx, ny):
                    continue
                if herb[nx][ny]:
                    continue
                if tree[nx][ny] == 0:
                    add_tree[nx][ny] += tree[i][j] // cnt

    # add_tree를 더해 번식을 동시에 진행시킵니다.
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            tree[i][j] += add_tree[i][j]


# 3단계 : 가장 많이 박멸되는 칸에 제초제를 뿌립니다.
def step_three():
    global ans

    dxs, dys = [-1, 1, 1, -1], [-1, -1, 1, 1]

    max_del, max_x, max_y = 0, 1, 1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # 모든 칸에 대해 제초제를 뿌려봅니다. 각 칸에서 제초제를 뿌릴 시 박멸되는 나무의 그루 수를 계산하고,
            # 이 값이 최대가 되는 지점을 찾아줍니다.
            if tree[i][j] <= 0:
                continue

            cnt = tree[i][j]
            for dx, dy in zip(dxs, dys):
                nx, ny = i, j
                for _ in range(k):
                    nx, ny = nx + dx, ny + dy
                    if is_out_range(nx, ny):
                        break
                    if tree[nx][ny] <= 0:
                        break
                    cnt += tree[nx][ny]

            if max_del < cnt:
                max_del = cnt
                max_x = i
                max_y = j

    ans += max_del

    # 찾은 칸에 제초제를 뿌립니다.
    if tree[max_x][max_y] > 0:
        tree[max_x][max_y] = 0
        herb[max_x][max_y] = c

        for dx, dy in zip(dxs, dys):
            nx, ny = max_x, max_y
            for _ in range(k):
                nx, ny = nx + dx, ny + dy
                if is_out_range(nx, ny):
                    break
                if tree[nx][ny] < 0:
                    break
                if tree[nx][ny] == 0:
                    herb[nx][ny] = c
                    break

                tree[nx][ny] = 0
                herb[nx][ny] = c


# 제초제의 기간을 1년 감소시킵니다.
def delete_herb():
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if herb[i][j] > 0:
                herb[i][j] -= 1


for _ in range(m):
    # 1단계 : 인접한 네 개의 칸 중 나무가 있는 칸의 수만큼 나무가 성장합니다.
    step_one()

    # 2단계 : 기존에 있었던 나무들은 아무것도 없는 칸에 번식을 진행합니다.
    step_two()

    # 제초제의 기간을 1년 감소시킵니다.
    delete_herb()

    # 3단계 : 가장 많이 박멸되는 칸에 제초제를 뿌립니다.
    step_three()

print(ans)

'''
# 내 풀이 - 틀림
# 0: 빈 칸, -1: 벽, 1 ~ 100 : 나무 수
n, m, k, c = map(int, input().split())  # 격자크기, 반복 수, 확산 범위, 제초제 지속 년 수
board = [list(map(int, input().split())) for _ in range(n)]
die = [[0 for _ in range(n)] for _ in range(n)]  # 제초제

dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]

def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    return True


def grow():
    # 0. 동시 성장
    temp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp[i][j] = board[i][j]

    # print('<<grow_temp>>')
    # for t in temp:
    #     print(*t)
    # print()

    # 1. 인접 네 칸 중 나무가 있는 칸 만큼 성장
    for x in range(n):
        for y in range(n):
            cnt = 0  # 인접한 나무의 개수
            if 1 <= board[x][y] <= 100:
                for dx, dy in zip(dxs, dys):
                    nx, ny = x + dx, y + dy
                    if in_range(nx, ny) and 1 <= board[nx][ny] <= 100:
                        cnt += 1

            temp[x][y] += cnt

    return temp


def add():
    # board[x][y] == 0 이면 번식
    # 0. 동시 성장
    temp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp[i][j] = board[i][j]

    # 1. 빈 칸의 개수 만큼 번식
    for x in range(n):
        for y in range(n):
            cnt = 0  # 빈 칸의 개수
            if 1 <= board[x][y] <= 100:
                # 번식 시작
                # 1-1. 빈 칸의 개수 세기 (빈 칸인 경우만)
                for dx, dy in zip(dxs, dys):
                    nx, ny = x + dx, y + dy
                    if in_range(nx, ny) and not board[nx][ny] and not die[nx][ny]:
                        cnt += 1

                # 1-2. 번식할 나무의 수 계산
                if cnt != 0:
                    trees = board[x][y] // cnt

                # 1-3. 번식
                for dx, dy in zip(dxs, dys):
                    nx, ny = x + dx, y + dy
                    if in_range(nx, ny) and not board[nx][ny] and not die[nx][ny]:
                        temp[nx][ny] += trees

    return temp


def use(x, y):

    print('======================================')
    print('<<input_board>>')
    for b in board:
        print(*b)
    print()

    temp_board = [[0 for _ in range(n)] for _ in range(n)]
    temp_die = [[0 for _ in range(n)] for _ in range(n)]

    # 복사
    for i in range(n):
        for j in range(n):
            temp_board[i][j] = board[i][j]
            temp_die[i][j] = die[i][j]

    # 초기 위치 처리
    cnt = board[x][y]
    temp_board[x][y] = 0
    temp_die[x][y] = k  # 현재 위치 제초제 뿌리기

    # 대각선
    for dx, dy in zip([-1, -1, 1, 1], [-1, 1, -1, 1]):
        wall = False
        while not wall:
            for i in range(1, k + 1):  #### 주의 범위, dx, dy 순서 (wall flag 진짜 멈추는지)
                nx, ny = x + (dx * i), y + (dy * i)

                if in_range(nx, ny):
                    # print(f'nx: {nx}, ny:{ny}, i(퍼진 범위): {i}')
                    # 1. 나무라면
                    if 1 <= board[nx][ny] <= 100:
                        cnt += board[nx][ny]
                        temp_board[nx][ny] = 0
                        temp_die[nx][ny] = k

                    # 2. 벽이면 멈추기
                    if board[nx][ny] == -1:
                        # temp_die[nx][ny] = k
                        wall = True
                        break
                    # 3. 빈 공간이라면 멈추고 제초제 뿌리기
                    if board[nx][ny] == 0:
                        temp_die[nx][ny] = k
                        wall = True
                        break
            wall = True


    print('<<제초 - baord>>')
    print(f'x:{x}, y:{y}')
    for t in temp_board:
        print(*t)
    print()

    print('<<제초 - die>>')
    for t in temp_die:
        print(*t)
    print()
    print(f'cnt:{cnt}')

    return temp_board, temp_die, cnt


def spread():
    global board, die
    temp_board = [[0 for _ in range(n)] for _ in range(n)]
    temp_die = [[0 for _ in range(n)] for _ in range(n)]
    max_die = -1
    mx, my = -1, -1
    loc = [] # (죽은 나무 수, mx, my)

    # 1. 제초제를 뿌렸을 때 가장 많은 나무가 죽는 위치 구하기
    for i in range(n):
        for j in range(n):
            if 1 <= board[i][j] <= 100:
                _, _, temp = use(i, j)
                if max_die < temp:
                    max_die = temp
                    # mx, my = i, j
                    loc.append((max_die, i, j))

    loc.sort(key = lambda x: (-x[0], x[1], x[2]))
    print(f'loc: {loc}')

    if not len(loc):
        return board, die, -1

    board, die, die_trees = use(loc[0][1], loc[0][2])

    # print('<<<<<<<<<결과 보드>>>>>>>>>>>')
    # for b in board:
    #     print(*b)
    # print()
    # print('<<<<<<<<<결과 제초제>>>>>>>>>>>')
    # for b in die:
    #     print(*b)


    return board, die, die_trees  # 박멸한 나무 그루 수


def after(die):
    for a in range(n):
        for b in range(n):
            if die[a][b]:
                die[a][b] -= 1

    return die

print('<<inital_board>>')
for b in board:
    print(*b)
print()

# main
ans = 0
for i in range(m):


    # 1. 성장
    board = grow()
    print('<<<<<<<<after_board>>>>>>>>>>>')
    for b in board:
        print(*b)
    print()
    # 2. 번식
    board = add()
    print('<<<<<<<<after_grow>>>>>>>>>>>')
    for b in board:
        print(*b)
    print()

    # 3. 제초
    print(f'반복 {i + 1}')
    if i > 0:
        die = after(die) # 제초제를 뿌리기 전 감소시킴
    board, die, die_trees = spread()
    if die_trees == -1:
        break # 모든 나무가 죽음

    ans += die_trees
    # ans += spread()

    print('<<<<<<<<<결과 보드>>>>>>>>>>>')
    for b in board:
        print(*b)
    print()
    print('<<<<<<<<<결과 제초제>>>>>>>>>>>')
    for b in die:
        print(*b)

    # 4. 제초제 유지 기간 감소 - 위치가 여기가 맞을까
    # die = after(die)
    print('<<after>>')
    for b in die:
        print(*b)
    print()

print('<<== 결과 ==>>')
print('<<board>>')
for b in board:
    print(*b)
print()
print('<<die>>')
for d in die:
    print(*d)

print('ans: ', end='')
print(ans)
'''