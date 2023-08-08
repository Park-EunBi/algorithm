# https://www.codetree.ai/missions/2/problems/conveyor-belt?utm_source=clipboard&utm_medium=text
# 시계방향으로 한 칸씩 회전하는 컨베이어 벨트 (1초에 한 칸씩)
# n : 윗 줄 숫자 개수, t: 회전 시간

n, t = map(int, input().split())
nums = []
for _ in range(2):
    nums.append(list(map(int, input().split())))

# 1차원 배열로 변경
# 받을 때 2차원으로 받지 말고 1차원 2개로 받은 뒤 '+' 해주면 된다
nums_one = []
for num in nums:
    nums_one += num

for _ in range(t):
    tmp_num = nums_one[-1]
    for i in range(2 * n -1, 0, -1):
        nums_one[i] = nums_one[i - 1]

    nums_one[0] = tmp_num


for num in nums_one[:n]:
    print(num, end= ' ')
print()
for num in nums_one[n:]:
    print(num, end=' ')

'''
# 다른 풀이 
# 2차원에서 그대로 이동시키는 방법 
temp = nums[0][-1]

# 1열 완성 시키기 
for i in range(n-1, 0, -1):
    nums[0][i] = nums[0][i - 1]
nums[0][0] = nums[1][-1]

# 2열 완성시키기 
for i in range(n-1, 0, -1):
    nums[1][i] = nums[1][i - 1]
nums[1][0] = temp
'''