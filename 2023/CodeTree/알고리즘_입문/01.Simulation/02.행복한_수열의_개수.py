# https://www.codetree.ai/missions/2/problems/number-of-happy-sequence?utm_source=clipboard&utm_medium=text
# 행복한 수열: 연속하여 m개 이상의 동일한 원소가 나오는 순간이 존재하는 수열
# 행복한 수열의 개수를 세어 출력 (각 행, 열 판단)

n, m = map(int, input().split())
nums = []
for _ in range(n):
    nums.append(list(map(int, input().split())))

ret = 0

# 행 판단
for i in range(n):
    count_col = 1
    max_col = 1
    for j in range(n - 1):
        if nums[i][j] == nums[i][j + 1]:
            count_col += 1
        # 틀린 이유 1. 연속 등장이 끝났을 때 값을 1로 초기화 하지 않았다
        else:
            count_col = 1
        # 틀린 이유 2. 행, 열의 최대 값을 저장해두지 않으면 다른 수가 나왔을 때 항상 1으로 값이 갱신된다
        max_col = max(max_col, count_col)

    if max_col >= m:
        ret += 1

# 열 판단
for j in range(n):
    count_row = 1
    max_row = 1
    for i in range(n - 1):
        if nums[i][j] == nums[i + 1][j]:
            count_row += 1
        # 틀린 이유 1. 연속 등장이 끝났을 때 값을 1로 초기화 하지 않았다
        else:
            count_row = 1
        # 틀린 이유 2. 행, 열의 최대 값을 저장해두지 않으면 다른 수가 나왔을 때 항상 1으로 값이 갱신된다
        # 틀린 이유 3. 최댓값 갱신은 두번재 for 문 안에서 진행되어야 한다
        max_row = max(max_row, count_row)

    if max_row >= m:
        ret += 1

print(ret)

'''
<testCase1>
6 3
1 1 2 2 3 3
2 3 4 5 6 1
3 4 5 6 1 2
4 5 6 1 2 3
5 6 1 2 3 4
6 1 2 3 4 5
'''

'''
<answer1>
0
'''

'''
<testCase2>
5 3
2 1 1 1 1
1 2 1 1 1
1 1 2 1 1
1 1 1 2 1
1 1 1 1 2
'''

'''
<answer2>
8
'''

'''
# <다른 풀이>
# 확인해야 할 수열을 통째로 함수로 넘겨 확인하는 방법 

def check():
    max_count, count = 1, 1
    for i in range(n-1):
        if seq[i] == seq[i + 1]:
            count += 1
        else:
            count = 1
        max_count = max(max_count, count)
    return max_count >= m

ret = 0
# 행 
for i in range(n):
    seq = [i][:] # 확인해야 할 부분을 통째로 넘긴다 
    if check: 
        ret += 1

# 열 
for j in range(n):
    for i in range(n):
        seq[i] = maps[i][j] # 열을 행으로 변경 (함수를 통해 확인하기 위해 일차원으로 변경)
    if check:
        ret += 1

print(ret)
'''