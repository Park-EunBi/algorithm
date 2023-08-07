# https://www.codetree.ai/missions/2/problems/gold-mining?utm_source=clipboard&utm_medium=text
# 채굴은 반드시 마름모 모양으로 한 번 가능
# 영역을 벗어나도 괜찮지만 영역 밖에는 금이 없다
# 채굴 비용 : 마름모 격자 개수 (k * k + (k + 1) * (k + 1))
# m: 금 한 개의 비용, 손해를 보지 않으면서 채굴할 수 있는 가장 많은 금의 개수 출력

n, m = map(int, input().split())
maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))


# solution 01. 모든 위치 확인하기
# 격자 내 임의의 점이 마름모에 포함되는지 -> 마름모의 정의 이용 (중심점, k 필요)
# 마름모의 중심 후보를 정하고, k의 후보에 대해 몇 개의 금이 포함되었는지 구하기
# 마름모: 중심점을 기준으로 k 번 이내로 인접한 곳으로 이동하며 갈 수 있는 곳
# (중심점과 x 거리의 차이 + 중심점과 y 사이의 거리) <= k
# k의 범위: k = 2 * (n -1)
# 전체 격자를 가능한 k 범위에 대해 모두 탐색한 뒤 최대 금의 개수를 저장

def get_area(k):
    return k * k + (k + 1) * (k + 1)


# 채굴 가능한 금의 개수
def get_gold(x, y, k):
    # 이중 for 문을 돌며 if 을 만족하는 i, j의 maps[i][j]을 구하고 누적합 구하기
    return sum([
        maps[i][j]
        for i in range(n)
        for j in range(n)
        # 마름모 안에 포함되는지 확인
        if abs(x - i) + abs(y - j) <= k
    ])


max_gold = 0

# 격자의 각 위치가 마름모의 중앙일 때 채굴 가능한 금의 개수 구하기
for row in range(n):
    for col in range(n):
        for k in range(2 * (n - 1) + 1):  # 빈 공간 없이 모든 공간을 커버하기 위해서는 k = 2*(n-1) 까지 커져야 한다
            gold = get_gold(row, col, k)

            # 손해를 보지 않으며 채굴할 수 있는 금의 최대 개수
            if gold * m >= get_area(k):
                max_gold = max(max_gold, gold)

print(max_gold)

'''
# solution 02. 마름모 내부만 확인하기 
# k = a 인 마름모를 탐색하려면 k = 0, 1, 2, ..., a - 1 까지 마름모의 가장자리를 누적해서 탐색하면 된다 

# get_area 함수는 solution 01과 동일 

# 해당 좌표가 격자에 포함되는지 반환
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and x < n

# 주어진 k에 대하여 채굴 가능한 금의 개수 반환 
def get_gold(i, j, k):
    gold = 0
    dxs, dys = [1, 1, -1, -1], [-1, 1, 1, -1]

    gold += maps[i][j] # k == 0 일 때의 예외처리 

    for curr_k in range(1, k + 1):
        curr_x, curr_y = row - curr_k, col # 순환 시작점 설정 
        for dx, dy in zip(dxs, dys):
            if in_range(curr_x, curr_y):
                gold += map[curr_x][curr_y]

            curr_x += dx
            curr_y += dy

    return gold

# main 코드는 solution 01과 동일 
'''

'''
# solution 03. 중복되는 경우 제외하여 효율적으로 탐색하기 
# k = a 일 때 내부 금의 개수: (k = a - 1 일 때의 금의 개수) + (k = a 마름모의 가장자리에 있는 금의 개수)
# 매번 마름모 안의 영역을 탐색하는 것이 아니라 이전에 탐색했던 마름모의 금 개수에 해당 마름모의 모서리 금 개수만을 더해주면 된다 

# get_area 함수는 solution 01과 동일 


# k에 대하여 채굴 가능 금의 개수 반환 
def get_num_of_gold_in_border(row, col, k):
    dxs, dys = [1, 1, -1, -1], [-1, 1, 1, -1]

    if k == 0:
        return grid[row][col]

    num_of_gold = 0

    curr_x, curr_y = row - k, col # 순회 시작점 설정
    for dx, dy in zip(dxs, dys):
        for step in range(k):
            if in_range(curr_x, curr_y):
                num_of_gold += grid[curr_x][curr_y]

            curr_x = curr_x + dx
            curr_y = curr_y + dy

    return num_of_gold

# main 코드는 solution 01과 동일 
'''
