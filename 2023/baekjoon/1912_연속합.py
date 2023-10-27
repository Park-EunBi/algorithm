n = int(input())
nums = list(map(int, input().split()))
# 현재까지의 합 vs 이전까지 합 중 최댓값 확인
for i in range(1, n):
    # 현재 값을 최댓 값으로 갱신
    nums[i] = max(nums[i], nums[i - 1] + nums[i])

print(max(nums))