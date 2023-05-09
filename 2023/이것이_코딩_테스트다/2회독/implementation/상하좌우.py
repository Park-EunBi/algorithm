# n x n 크기의 정사각형 공간
# 가장 왼쪽 위 (1, 1)
# 가장 오른쪽 아래 (n, n)
# L R U D 이동
# 공간을 넘어가는 움직임 -> 무시

n = int(input())
moves = list(input().split())

# 초기 좌표
x, y = 1, 1
# 방향 설정
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']
nx, ny = 1, 1

for m in moves:
    for i in range(len(move_types)):
        # 이동 방식 선택
        if m == move_types[i]:
            # nx, ny에 임시 위치 저장
            nx = x + dx[i]
            ny = y + dy[i]

        # 임시 위치가 범위를 넘어서면 갱신 안함
        if nx < 1 or nx > n or ny < 1 or ny > n:
            continue

        # 임시 위치가 범위 내에 존재한다면 좌표 갱신
        x, y = nx, ny

        
print(x, y)


'''
<testCase>
5
R R R U D D
<answer>
3 4
'''