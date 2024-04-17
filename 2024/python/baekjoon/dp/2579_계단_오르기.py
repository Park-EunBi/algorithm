n = int(input())
stair = [int(input()) for _ in range(n)]
stair.append(0) # 계단이 1개 주어졌을 때 index error 방지

# sol_1
# 1. dp  정의 하기
# d[i][j]: j개의 계단을 연속해서 밟고 i 번째 계단에 도착할 수 있는 점수의 최댓값
dp = [[0, 0] for _ in range(301)]

# 2. 초기화
dp[0][0] = stair[0]
dp[1][0] = stair[1]
dp[1][1] = stair[0] + stair[1]

# 3. 점화식
for i in range(2, n):
    dp[i][0] = max(dp[i-2][0] + stair[i], dp[i-2][1] + stair[i])
    dp[i][1] = dp[i-1][0] + stair[i]

print(max(dp[n-1]))

# sol_2
#1. dp 정의하기
# d[i]: i 번째 계단에 올라섰을 때 밟지 않을 계단의 합의 최솟값
# i 번째 계단은 밟지 않을 것임
dp = [0 for _ in range(302)]

# 2. 초기화
dp[1] = stair[1]
dp[2] = stair[2]
dp[3] = stair[3]

# 3. 점화식
for i in range(4, n + 1):
    # i 번째 계단을 밟지 않으려면
    # i-2 혹은 i-3 번째 계단 중에 하나를 밟지 않아야 한다
    dp[i] = min(dp[i - 2], dp[i - 3]) + stair[i]

print(sum(stair) - min(dp[i-1], dp[i-2]))