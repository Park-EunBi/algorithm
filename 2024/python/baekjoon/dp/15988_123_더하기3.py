n = int(input())

# dp[i]: i를 1, 2, 3의 합으로 나타내는 경우의 수
dp = [0 for _ in range(1000001)]

# 초기화
dp[0] = 1
dp[1] = 1
dp[2] = 2

# 점화식
for i in range(3, 1000001):
    dp[i] = dp[i-1] % 1000000009+ dp[i-2] % 1000000009 + dp[i-3] % 1000000009

for i in range(n):
    num = int(input())
    print(dp[num] % 1000000009)