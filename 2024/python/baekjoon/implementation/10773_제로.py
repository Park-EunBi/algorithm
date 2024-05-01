import sys
input = sys.stdin.readline

n = int(input())
nums = []
for _ in range(n):
    num = int(input())
    if not num:
        nums.pop(-1)
    else:
        nums.append(num)

print(sum(nums))