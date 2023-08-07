# https://www.codetree.ai/missions/2/problems/slanted-rectangle/description?utm_source=clipboard&utm_medium=text
# 기울어진 직사각형: 한 지점으로 부터 대각선으로 움직이며 반시계 순회를 했을 대 지나왔던 지점들의 집합
# 반드시 아래에서 시작하여 반시계 방향으로 순회해야 하며, 각 방향으로 최소 1번 이동해야 한다. (격자 넘어서면 안된다)
# 기울어진 직사각형을 이루는 지점의 수의 합이 최대가 되도록 작성

n = int(input())
nums = []
for _ in range(n):
    nums.append(list(map(int, input().split())))


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


def get_score(x, y, k, l):
    dxs, dys = [-1, -1, 1, 1], [1, -1, -1, 1]
    move_nums = [k, l, k, l]

    sum_nums = 0

    # 경계 따라가기
    for dx, dy, move_num in zip(dxs, dys, move_nums):
        for _ in range(move_num):
            x, y = x + dx, y + dy

            # 경계를 벗어나면 0 반환
            if not in_range(x, y):
                return 0

            sum_nums += nums[x][y]
    return sum_nums


ret = 0
# (i, j) -> 1, 2, 3, 4 방향
# [k, 1, k, 1] 만큼 이동하며 직사각형 그리기
for i in range(n):
    for j in range(n):
        for k in range(1, n):
            for l in range(1, n):
                ret = max(ret, get_score(i, j, k, l))

print(ret)

# 시작 지점을 순회하며 변의 크기를 하나씩 늘려가기
# (2, 1) -> (n, n) 까지 가능

# 방향 1: (i - 1, j + 1)
# 방향 2: (i - 1, j - 1)
# 방향 3: (i + 1, j - 1)
# 방향 4: (i + 1, j + 1)

# dxs = [-1, -1, 1, 1]
# dys = [1, -1, -1, 1]

# max_sum = 0

'''
# 2 * 2 마름모 이동 
for col in range(2, n):
    for row in range(1, n-1):
        temp_sum = 0 
        for dx, dy in zip(dxs, dys):
            if col + dx < 0 or col + dx >= n or row + dy < 0 or row + dy >= n:
                break
            col += dx
            row += dy

            temp_sum += nums[col][row]

        print('temp_sum: ', temp_sum)
        max_sum = max(max_sum, temp_sum)
print('max_sum: ', max_sum)
'''
'''
# 나의 풀이 - 틀림 
# 가로 증가 
for i in range(1, n-1): # n-2까지 늘릴 수 있어서 
    # 세로 증가 
    for j in range(1, n-1):
        for col in range(2, n):
            for row in range(1, n-1):
                temp_sum = 0 
                for dx, dy in zip(dxs, dys):
                    if col + (dx * i) < 0 or col + (dx * i) >= n or row + (dy * j) < 0 or row + (dy * j) >= n:
                        break
                    col += (dx * i)
                    row += (dy * j)

                    temp_sum += nums[col][row]
                # print('temp_sum: ', i, j, col, row, temp_sum)
                max_sum = max(max_sum, temp_sum)
        # print('max_sum: ', max_sum)
print(max_sum)
'''