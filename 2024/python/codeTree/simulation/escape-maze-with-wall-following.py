# '#': 벽, '.': 빈 공간
n = int(input())
x, y = map(int, input().split())
board = [list(''.join(input().split())) for _ in range(n)]

x -= 1
y -= 1
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0] # 우 하 좌 상 (시계 방향)
time = 0
direction = 0 # 우
cnt = 0 # 사방 이동 확인 - 현재 자리에서 4번 확인했는지 보는 것, 초기화 주의

def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    return True

def simulaton(x, y):
    global direction, time, cnt
    nx, ny = x + dxs[direction], y + dys[direction]

    # 1. 현재 방향으로 이동 불가
    if in_range(nx, ny) and board[nx][ny] == '#':
        # 반시계 방향으로 회전
        direction = (direction -1) % 4
        cnt += 1
        return x, y
    # 2. 이동은 가능하나 격자 밖이라면 - 탈출
    elif not in_range(nx, ny):
        cnt = 0
        time += 1
        x, y = nx, ny
        return x, y

    # 3. 이동 가능하고
    elif in_range(nx, ny) and board[nx][ny] == '.':
        cnt = 0
        # 3-1. 오른쪽(시계방향)에 짚을 벽이 있다면
        rd = (direction + 1) % 4  # right direction
        rx, ry = nx + dxs[rd], ny + dys[rd]

        if board[rx][ry] == '#':
            # 그 뱡향으로 이동
            time += 1
            x, y = nx, ny

            return x, y

        # 3-2. 오른쪽에 벽이 없다면
        if board[rx][ry] == '.':
            # 현재 방향으로 한 칸 이동
            time += 1
            # 회전 후 전진
            time += 1

            direction = rd
            x, y = rx, ry
            return x, y

    return x, y

while in_range(x, y):
    x, y = simulaton(x, y)
    # 길이 없을 경우
    if time > n * n or cnt > 4:
        time = -1
        break

print(time)

'''
3
2 2
.#.
#.#
.#.

-1
'''

# 탈출이 불가능한 경우를 판단하기 위해서 (현재 윛, 현재 바라보고 있는 방향) 상태라 중복되는지를 살펴봐야 함
# -> 탈출이 불가능하면 계속 같은 위치를 맴돎 -> visited 배열 사용
'''
# 각 방향별로 visited 배열을 만듦
visited = [
    [
        [False for _ in range(DIR_NUM)]
        for _ in range(n + 1)
    ]
    for _ in range(n + 1)
]
'''