n = int(input())

# dp[i] : 2 x N 의 사각형을 채우는 가짓수
dp = [0] * 1001

# 초기화
dp[1] = 1
dp[2] = 3

# 점화식 - dp[i] = dp[i-1] + dp[i-2] * 2
for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2] * 2

print(dp[n] % 10007)
