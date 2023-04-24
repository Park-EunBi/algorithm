import sys
sys.stdin = open("input.txt", "rt")

# 전형적인 구현 문제
# 방향을 설정해서 문제를 풀 땐 dx, dy 리스트를 만들어 방향을 정하는 것이 좋다

n, m = map(int, input().split())

# 방문 리스트
d = [[0] * m for _ in range(n)] # 컴프리헨션 (2차원 리스트 만들때 자주 사용)
x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 위치 방문 처리

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left() :
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while 1:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전 후 가보지 않은 칸이 있을 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] =1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수있음 이동
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else :
            break
        turn_time = 0
print(count)


'''
# 오답
n, m = map(int, input().split())

# 현재 좌표와 바라보는 방향 0: 북 1:동 2 : 남 3: 서
x, y, compose = map(int, input().split())
sea = []
res = 0 # 방문한 칸의 개수
# 육지(0), 바다(1) 정보
for i in range(n):
   sea.append(list(map(int, input().split())))

check_map = []

# 0000
# 0000
# 0000
# 0000

for i in range(m):
    check_map.append([0] * m)

now = [1,1]
dx = now[0]
dy = now[1]
cnt = 0 # 회전 횟수 기록

while 1:
    # 1. 왼쪽 방향에 가보지 않은 곳이 있다면 회전하고, 그 곳으로 이동
    if compose == 0:
        dy -= 1
    elif compose == 1:
        dx -=1
    elif compose == 2:
        dy += 1
    elif compose == 3:
        dx += 1

    if check_map[dx][dy] == 0:
        now[x] = dx
        now[y] = dy
        check_map[dx][dy] = 1

        if compose != 0:
            compose -= 1
        else:
            compose = 3

    # 2. 모든 방향이 갔던 곳이면 한칸 뒤로 가기
    else:
        cnt += 1
        if cnt == 5:
            # 4번 다 돌았는데 못감
            if compose == 0:
                dx += 1
            elif compose == 1:
                dy -= 1
            elif compose == 2:
                dx -= 1
            elif compose == 3:
                dy += 1

            if check_map[dx][dy] == 0:
                now[x] = dx
                now[y] = dy
    if now[x] < 1 or now[y] < 1 or now[x] > n or now[y] > m:
        break

print(check_map)
'''