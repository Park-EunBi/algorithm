# n x m 크기의 직사각형
# (a, b) a: 북쪽에서 떨어진 칸의 개수, b: 서쪽으로
# 상하좌우 이동, 바다는 못감

# 이동 방식
## 왼쪽에 가보지 않은 곳 있으면 왼쪽으로 1칸 전진
## 가본 칸이라면 왼쪽으로 한번 더 이동
## 모두 가본 곳이거나 바다이면 바라보는 방향 유지 후
## 뒤로 한칸 (뒤도 바다면 멈춤)

n, m = map(int, input().split())
# direction: 0 - n, 1 - e, 2 - s, 3 - w
x, y, direction = map(int, input().split())
# 0: land, 1: sea
area = []
for _ in range(n):
    area.append(list(map(int, input().split())))

# n, e, s, w
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 방향 설정
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0
# 방문 위치 저장
d = [[0] * m for _ in range(n)]
# 현재 위치 방문 처리
d[x][y] = 1
while 1:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 정면에 가보지 않은 칸이 있는 경우
    if d[nx][ny] == 0 and area[nx][ny] == 0:
        # 방문 표시
        d[nx][ny] = 1
        x, y = nx, ny
        count += 1
        turn_time = 0
        continue
    # 가본 곳이거나 바다인 경우
    else:
        turn_time += 1
    # 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 이동
        if area[nx][ny] == 0:
            x, y = nx, ny
        # 바다인 경우
        else:
            break
        turn_time = 0

print(count)






'''
<testCase>
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
<answer>
3
'''
