# https://www.codetree.ai/missions/2/problems/The-2D-wind-blows?utm_source=clipboard&utm_medium=text
# 1. 영역 내 숫자 시계 방향으로 회전
# 2. 영역 내 숫자 주변 평균 값으로 변경

# q: 바람이 불어오는 횟수
n, m, q = tuple(map(int, input().split()))
a = [
    [0 for _ in range(m + 1)]
    for _ in range(n + 1)
]
temp_arr = [
    [0 for _ in range(m + 1)]
    for _ in range(n + 1)
]


# 시계방향 회전
def rotate(start_row, start_col, end_row, end_col):
    temp = a[start_row][start_col]

    # 1. 하 -> 상
    for row in range(start_row, end_row):
        a[row][start_col] = a[row + 1][start_col]

    # 2. 우 -> 좌
    for col in range(start_col, end_col):
        a[end_row][col] = a[end_row][col + 1]

    # 3. 상 -> 하
    for row in range(end_row, start_row, -1):
        a[row][end_col] = a[row - 1][end_col]

    # 4. 좌 -> 우
    for col in range(end_col, start_col, -1):
        a[start_row][col] = a[start_row][col - 1]

    a[start_row][start_col + 1] = temp


# 범위 확인
def in_range(x, y):
    return 1 <= x and x <= n and 1 <= y and y <= m


# 인접 숫자들의 평균 값 계산
def average(x, y):
    # 자신 포함 상하좌우 -> 방향 5개 처리
    dxs, dys = [0, 1, -1, 0, 0], [0, 0, 0, 1, -1]

    active_numbers = [
        a[x + dx][y + dy]
        for dx, dy in zip(dxs, dys)
        if in_range(x + dx, y + dy)
    ]

    return sum(active_numbers) // len(active_numbers)


# 평균값으로 변경
def set_average(start_row, start_col, end_row, end_col):
    # temp_arr에 평균값 저장
    for row in range(start_row, end_row + 1):
        for col in range(start_col, end_col + 1):
            temp_arr[row][col] = average(row, col)

    # temp_arr의 값을 다시 가져옴
    for row in range(start_row, end_row + 1):
        for col in range(start_col, end_col + 1):
            a[row][col] = temp_arr[row][col]


# 시뮬레이션
def simulate(start_row, start_col, end_row, end_col):
    rotate(start_row, start_col, end_row, end_col)
    set_average(start_row, start_col, end_row, end_col)


for row in range(1, n + 1):
    given_nums = list(map(int, input().split()))
    for col, num in enumerate(given_nums, start=1):
        a[row][col] = num

for _ in range(q):
    r1, c1, r2, c2 = tuple(map(int, input().split()))

    simulate(r1, c1, r2, c2)

for row in range(1, n + 1):
    for col in range(1, m + 1):
        print(a[row][col], end=" ")
    print()