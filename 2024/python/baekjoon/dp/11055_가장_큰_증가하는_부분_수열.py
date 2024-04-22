n = int(input())
nums = list(map(int, input().split()))

# dp[i]: i부터 시작하는 증가하는 부분 수열의 합
dp = [0] * n

# 초기화
dp[0] = nums[0]

# 점화식
for i in range(1, n):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j] + nums[i])
        else:
            dp[i] = max(dp[i], nums[i])

print(max(dp))