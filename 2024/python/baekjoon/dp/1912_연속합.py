import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

# dp[i]: i 번째 수를 선택했을 때의 최대 합
dp = [0] * n

# 초기화
dp[0] = nums[0]

# 점화식: dp[i]: max(dp[i-1] + nums[i], nums[i])
for i in range(1, n):
    dp[i] = max(dp[i-1] + nums[i], nums[i])

print(max(dp))