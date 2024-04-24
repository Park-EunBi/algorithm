n, k = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0
for i in range(n-1, -1, -1):
    mx = max(nums[:i + 1])
    idx = nums.index(mx)
    temp = nums[i]

    if mx != nums[i]:
        nums[i], nums[idx] = nums[idx], nums[i]
        cnt += 1

    if cnt == k:
        print(temp, mx)
        break

else:
    print(-1)