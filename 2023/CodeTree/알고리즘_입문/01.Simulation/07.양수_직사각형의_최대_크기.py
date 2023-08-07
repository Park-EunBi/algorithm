# https://www.codetree.ai/missions/2/problems/max-area-of-positive-rectangle?utm_source=clipboard&utm_medium=text
# 가능한 양수 직사각형 중 최대 크기
# 양수 직사각형: 격자 판에 평행한 직사각형이면서 내부 숫자가 모두 양수인 직사각형

n, m = map(int, input().split())
nums = []
for _ in range(n):
    nums.append(list(map(int, input().split())))

max_size = -1

def in_range(x, y):
    if 0 <= x and x < n and 0 <= y and y < m:
        return True
    return False


# 직사각형 내 양수인지 확인 (직사각형을 움직이진 않음)
def check_positive(x, y, col, row):
    for i in range(x, x + col):
        for j in range(y, y + row):
            if not in_range(i, j):
                return -1 # break 하면 안된다 (for 문 1개만 나감)
            if nums[i][j] <= 0: # 0 도 양수가 아닌 것으로 침
                return -1
    return col * row



for x in range(n):
    for y in range(m): # n이 아니라 m
        for col in range(1, n + 1): # + 1 해주어야 한다 (가로, 세로 길이라서)
            for row in range(1, m + 1):
                temp_size = check_positive(x, y, col, row)
                max_size = max(max_size, temp_size)

print(max_size)

'''
# 다른 풀이 
# all 사용 
def positive_rect(x1, y1, x2, y2):
    return all([
        grid[i][j] > 0
        for i in range(x1, x2 + 1)
        for j in range(y1, y2 + 1)
    ])
'''