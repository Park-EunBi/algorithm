n = int(input())

# 1. dp 정의 하기
# dp[i]: i 번째 까지 타일을 채울 수 있는 가짓수
dp = [0] * (n + 1)
dp.append(0)
dp.append(0)
# 2. 초기화
dp[1] = 1
dp[2] = 2

# 점화식
for i in range(3, n + 1):
    dp[i] = dp[i-2] + dp[i-1]

print(dp[n] % 10007)