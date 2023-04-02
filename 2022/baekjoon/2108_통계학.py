import math
n = int(input())
nums = []
for _ in range(n): nums.append(int(input()))


print(round(sum(nums)/len(nums)))

nums.sort()
print(nums[int((n-1)/2)])

