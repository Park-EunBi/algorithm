n = int(input())
nums = list(map(int, input().split()))

sorted_nums = sorted(list(set(nums)))

dict = {}
for i in range(len(sorted_nums)):
    dict[sorted_nums[i]] = i

for num in nums:
    print(dict[num], end = ' ')