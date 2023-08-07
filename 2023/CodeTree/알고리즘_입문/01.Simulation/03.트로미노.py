# https://www.codetree.ai/missions/2/problems/tromino?utm_source=clipboard&utm_medium=text
# 두 개의 블럭을 적당이 놓아 놓인 칸에 적힌 숫자의 합이 최대가 될 때의 결과 출력
# 블럭 회전 가능
# 블록 1: ㄴ 자 모양, 블록 2: ㅡ 자 모양 (둘 다 3칸)

n, m = map(int, input().split())
nums = []
for _ in range(n):
    nums.append(list(map(int, input().split())))

# 'ㄴ' rotate sample
# (0, 0) (1, 0) (1, 1)
# (0, 0) (0, 1) (1, 0)
# (0, 0) (0, 1) (1, 1)
# (0, 1) (1, 0) (1, 1)
# => 해당하지 않는 곳을 제외하기
# (i, i) ~ (i + 1, i + 1) 에서 한 블록식 제거해서 rotate 구현

max_sum = 0

# 'ㄴ' 블록 회전시 합계의 최댓값 반환
def check_chair(x, y):
    max_chair = 0
    sum_square = 0

    for i in range(x, x + 2):
        for j in range(y, y + 2):
            sum_square += nums[i][j]

    # 회전 - 한 블록의 값 제거
    for i in range(x, x + 2):
        for j in range(y, y + 2):
            max_chair = max(max_chair, sum_square - nums[i][j])
    return max_chair


# 'ㅡ' 자형 블록
def check_line_col(x, y):
    sum_col = 0
    for i in range(y, y + 3):
        sum_col += nums[x][i]
    return sum_col


# 'ㅣ' 자형 블록
def check_line_row(x, y):
    sum_row = 0
    for i in range(x, x + 3):
        sum_row += nums[i][y]
    return sum_row


# 'ㄴ' 먼저 판단
for i in range(n - 1):
    for j in range(m - 1):
        max_sum = max(max_sum, check_chair(i, j))

# 'ㅡ'
for i in range(n):
    for j in range(m - 2):
        max_sum = max(max_sum, check_line_col(i, j))

# 'ㅣ'
for i in range(n - 2):
    for j in range(m):
        max_sum = max(max_sum, check_line_row(i, j))

print(max_sum)

'''
<testCase1>
3 3
1 2 3
3 2 1
3 1 1

<answer1>
8

<testCase2>
4 5
6 5 4 3 1
3 4 4 14 1
6 1 3 15 5
3 5 1 16 3

<answer2>
45
'''

'''
# 다른 풀이 
# 각 블럭을 회전할 수 있는 경우의 수는 총 6가지 
# 6가지를 모두 담을 수 있는 배열을 사용하여 탐색 

# 모든 경우의 수 
shapes = [
    [[1, 1, 0],
    [1, 0, 0],
    [0, 0, 0]],

    [[1, 1, 0],
    [0, 1, 0],
    [0, 0, 0]],

    [[1, 0, 0],
    [1, 1, 0],
    [0, 0, 0]],

    [[0, 1, 0],
    [1, 1, 0],
    [0, 0, 0]],

    [[1, 1, 1],
    [0, 0, 0],
    [0, 0, 0]],

    [[1, 0, 0],
    [1, 0, 0],
    [1, 0, 0]],
]

# 탐색 
def get_max(x, y):
    max_sum = 0
    for i in range(6):
        is_ok = True
        temp_sum = 0
        
        for j in range(0, 3):
            for k in range(0, 3):
                # 더해줄 값이 없다면 (블록이 위치한 곳이 아닐 경우)
                if shapes[i][j][k] == 0:
                    continue
                # 범위 확인 
                if x + j >= n or y + k >= m:
                    is_ok = False
                # 블록이 위치하여 계산이 가능하다면 
                else:
                    # 해당 위치의 값 누적합
                    temp_sum += nums[x + j][y + k]
            # 계산 가능했다면 
            if is_ok:
                # 최댓값 갱신
                temp_num = max(max_sum, temp_sum)
    return max_sum
    
ret = 0

for i in range(n):
    for j in range(m):
        ret = max(ret, get_max(i, j))

print(ret)
'''