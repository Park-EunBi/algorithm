import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

# dp[i]: i 번째 까지 수의 합
dp = [0 for _ in range(n)]

# 초기화
dp[0] = nums[0]

# 점화식
for i in range(1, n):
    dp[i] = dp[i-1] + nums[i]
dp.insert(0, 0)

for _ in range(m):
    i, j = map(lambda x: int(x)-1, input().split())
    print(dp[j + 1] - dp[i])