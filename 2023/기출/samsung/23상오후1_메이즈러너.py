# n: 미로의 크기, m: 참가자 수, k: 게임 시간

# input
n, m, k = tuple(map(int, input().split()))
board = [
    [0] * (n + 1)
    for _ in range(n + 1)
]

for i in range(1, n + 1):
    board[i] = [0] + list(map(int, input().split()))

# 회전을 위한 2차원 배열 - 0으로 채워진 2차원 배열
next_board = [
    [0] * (n + 1)
    for _ in range(n + 1)
]

# 참가자의 위치 정보
# 참가자 번호 1번부터 시작하도록 [(-1, -1)] 더해줌
traveler = [(-1, -1)] + [
    tuple(map(int, input().split()))
    for _ in range(m)
]

# 출구 위치 정보
exits = tuple(map(int, input().split()))

# 모든 참가자들의 이동 거리 합
ans = 0

# 회전해야 하는 최소 정사각형
sx, sy, square_size = 0, 0, 0


# 모든 참가자 이동
def move_all_traveler():
    global exits, ans

    # m 명의 참가자 이동
    for i in range(1, m + 1):
        # 출구 도착 확인
        if traveler[i] == exits:
            continue

        tx, ty = traveler[i]
        ex, ey = exits

        # 행이 다른 경우 행 이동
        # '움직일 수 있는 칸이 2개 이상이라면, 상하로 움직이는 것을 우선시합니다.'
        if tx != ex:
            nx, ny = tx, ty

            # 출구가 아래에 있다면
            if ex > nx:
                nx += 1
            else:
                nx -= 1

            # 벽이 없다면 행을 이동
            # 행 이동 후 다음 참가자로
            if not board[nx][ny]:
                traveler[i] = (nx, ny)
                ans += 1
                continue

        # 열이 다른 경우 열 이동
        if ty != ey:
            nx, ny = tx, ty

            if ey > ny:
                ny += 1
            else:
                ny -= 1

            # 벽이 없다면 행 이동
            # 열 이동시키기
            if not board[nx][ny]:
                traveler[i] = (nx, ny)
                ans += 1
                continue


# 사각형을 만들며 참가자와 출구가 있는지 확인하는 방식

# 한 명 이상의 참가자와 출구를 포함한 가장 작은 정사각형 찾기
def find_minimum_square():
    global exits, sx, sy, square_size
    ex, ey = exits

    # 가장 작은 정사각형부터 모든 정사각형 만들기
    for sz in range(2, n + 1):
        # 좌상단 r 좌표가 작은 것 부터
        for x1 in range(1, n - sz + 2):
            # 좌상단 c의 좌표가 작은 것 부터
            for y1 in range(1, n - sz + 2):
                x2, y2 = x1 + sz - 1, y1 + sz - 1

                # 출구가 정사각형 안에 없다면 pass
                if not (x1 <= ex and ex <= x2 and y1 <= ey and ey <= y2):
                    continue

                # 한 명 이상의 참가자가 정사각형에 있는지 판단
                is_traveler_in = False
                for l in range(1, m + 1):
                    tx, ty = traveler[l]
                    if x1 <= tx and tx <= x2 and y1 <= ty and ty <= y2:
                        # 출구에 있는 참가자 제외
                        if not (tx == ex and ty == ey):
                            is_traveler_in = True

                # 한 명 이상의 참가자가 정사각형 안에 있다면
                # 정보 갱신 후 종료
                if is_traveler_in:
                    sx = x1
                    sy = y1
                    square_size = sz

                    return

# 정사각형 내부 벽 회전
def rotate_square():
    # 벽돌 감소
    for x in range(sx, sx + square_size):
        for y in range(sy, sy + square_size):
            if board[x][y]:
                board[x][y] -= 1

    # 정사각형 회전
    for x in range(sx, sx + square_size):
        for y in range(sy, sy + square_size):
            # Step 1. (sx, sy)를 (0, 0)으로 옮겨주는 변환
            ox, oy = x - sx, y - sy
            # Step 2. 변환된 상태에서는 회전 이후의 좌표가 (x, y) . (y, square_n - x - 1)가 된다
            rx, ry = oy, square_size - ox - 1
            # Step 3. 다시 (sx, sy) 더하기
            next_board[rx + sx][ry + sy] = board[x][y]

    # next_board (회전한 보드)를 현재 board에 옮기기
    for x in range(sx, sx + square_size):
        for y in range(sy, sy + square_size):
            board[x][y] = next_board[x][y]


# 모든 참가자들 및 출구 회전
def rotate_traveler_and_exit():
    global exits

    # m 명의 참가자 모두 확인
    for i in range(1, m + 1):
        tx, ty = traveler[i]
        # 참가자가 정사각형 안에 포함되어 있을 때만 회전
        if sx <= tx and tx < sx + square_size and sy <= ty and ty < sy + square_size:
            # Step 1. (sx, sy)를 (0, 0)으로 옮겨주는 변환
            ox, oy = tx - sx, ty - sy
            # Step 2. 변환된 상태에서는 회전 이후의 좌표가 (x, y) . (y, square_n - x - 1) 된다
            rx, ry = oy, square_size - ox - 1
            # Step 3. 다시 (sx, sy)를 더하기
            traveler[i] = (rx + sx, ry + sy)

    # 출구 회전
    ex, ey = exits
    if sx <= ex and ex < sx + square_size and sy <= ey and ey < sy + square_size:
        # Step 1. (sx, sy)를 (0, 0)으로 옮겨주는 변환
        ox, oy = ex - sx, ey - sy
        # Step 2. 변환된 상태에서는 회전 이후의 좌표가 (x, y) . (y, square_n - x - 1)가 된다
        rx, ry = oy, square_size - ox - 1
        # Step 3. 다시 (sx, sy)를 더하기
        exits = (rx + sx, ry + sy)


for _ in range(k):
    # 모든 참가자 이동
    move_all_traveler()
    # 모든 사람이 출구로 탈출했는지 확인
    is_all_escaped = True
    for i in range(1, m + 1):
        if traveler[i] != exits:
            is_all_escaped = False

    # 모든 사람이 탈출했으면
    if is_all_escaped:
        break

    # 한 명 이상의 참가자와 출구를 포함한 가장 작은 정사각형 찾기
    find_minimum_square()

    # 정사각형 내부 벽 회전
    rotate_square()

    # 모든 참가자 및 출구 회전
    rotate_traveler_and_exit()

print(ans)

ex, ey = exits
print(ex, ey)











