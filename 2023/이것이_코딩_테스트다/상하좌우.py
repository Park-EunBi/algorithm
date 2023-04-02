import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
move = list(map(str, input().split()))

start = [1, 1]
for m in move:
    if m == 'L' and start[1] > 1 and start[1] <= 5:
        start[1] -= 1
    elif m == 'R' and start[1] >= 1 and start[1] < 5:
        start[1] += 1
    elif m == 'U' and start[0] > 1 and start [0] <= 5:
        start[0] -= 1
    elif m == 'D' and start[0] >=1 and start[0] < 5:
        start[0] += 1

print(start)

'''
# 다른 풀이 

x, y = 1, 1
plans = input().split()

# L, R, U, D 에 따른 이동 방향 
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_type = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_type)):
        if plan == move_type[i]:
            nx = x + dx[i]
            my = y + dy[i]
        
        # 공간을 넘어가는 경우 
        if nx < 1 or ny < 1 or nx > n or ny >n:
            continue:
        # 이동 
        x, y = nx, ny
print(x, y)
'''
