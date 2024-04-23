t = int(input())
nums = [int(input()) for _ in range(t)]
n = max(nums)

# dp[i] : i 번째 삼각형의 한 변의 길이
dp = [0] * (n + 1)

# 초기화
dp[0] = 1
dp[1] = 1
dp[2] = 1

# 점화식
for i in range(3, n + 1):
    dp[i] = dp[i-2] + dp[i-3]

for num in nums:
    print(dp[num-1])