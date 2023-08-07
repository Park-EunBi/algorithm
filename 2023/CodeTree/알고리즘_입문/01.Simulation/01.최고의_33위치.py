# https://www.codetree.ai/missions/2/problems/best-place-of-33?utm_source=clipboard&utm_medium=text
# 1: 동전 O, 0: 동전 X
# 최대로 얻을 수 있는 동전의 수

n = int(input())
maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

money = 0

# 3 * 3 격자 내 최대 금액 확인
def check_money(array, x, y):
    temp_money = 0

    for i in range(x, x + 3):
        for j in range(y, y + 3):
            temp_money += array[i][j]
    return temp_money

# 3 * 3 격자 넘어가지 않도록 탐색
for i in range(n - 2):
    for j in range(n - 2):
        money = max(money, check_money(maps, i, j))

print(money)

'''
<testCase>
3
1 0 1
0 1 0
0 1 0
'''

'''
<answer>
4
'''