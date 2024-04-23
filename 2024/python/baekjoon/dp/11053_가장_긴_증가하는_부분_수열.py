n = int(input())
nums = list(map(int, input().split()))

# dp[i]: i 번째 수를 포함했을 때 수열의 최대 길이
dp = [0] * n

# 점화식
for i in range(n):
    mx = 0
    for j in range(i): # i 번째 이전에 nums[i] 보다 작은 수가 있었는지 체크
        if nums[i] > nums[j]: # 나보다 작은 수가 있다면
            mx = max(mx, dp[j]) # 작은 수 중 최댓값을 찾아서 mx로 저장
    dp[i] = mx + 1

print(max(dp))