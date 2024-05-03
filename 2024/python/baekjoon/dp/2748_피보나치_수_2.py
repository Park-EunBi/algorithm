n = int(input())

# dp[i]: i 번째 피보나치 수
dp = [0] * 91

# 초기화
dp[1] = 1
dp[2] = 1

# 점화식
for i in range(3, n + 1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])