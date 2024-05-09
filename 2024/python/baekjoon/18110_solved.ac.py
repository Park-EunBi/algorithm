import sys
input = sys.stdin.readline

n = int(input())

if n == 0:
    print(0)
    exit(0)

nums = [int(input()) for _ in range(n)]
nums.sort()

def round(num):
    return (int(num) + (1 if num - int(num) >= 0.5 else 0))

temp = int(n * 0.15 + 0.5)
ret = 0
for i in range(temp, n - temp):
    ret += nums[i]

print(int(ret / (n - 2 * temp) + 0.5))

# # nums = nums[int(n * 0.15 + 0.5): int(n * 0.75 + 0.5)] # 슬라이스 하면 안된다
# # print(int(sum(nums)/len(nums) + 0.5))