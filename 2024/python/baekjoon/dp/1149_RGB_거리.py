n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]

# 1. dp 정의: [i]번째 집을 [j]번째 색으로 칠했을 때의 최소 비용
dp = [[0 for _ in range(3)] for _ in range(n)]

# 2. 초기화
dp[0] = costs[0]

# 3. 점화식
for i in range(1, n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]

print(min(dp[-1]))