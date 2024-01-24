import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
nums.sort()
ret = 0

for i in range(n):
    find_num = nums[:i] + nums[i+1:] # 자기 자신 제외
    start, end = 0, len(find_num) - 1

    while start < end:
        total = find_num[start] + find_num[end]
        if total == nums[i]: # nums[i] == target
            ret += 1
            break
        elif total < nums[i]:
            start += 1
        else:
            end -= 1


print(ret)