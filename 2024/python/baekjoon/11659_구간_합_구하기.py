import sys
input= sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
sum_list = [0] * (n + 1)

for i in range(1, n + 1):
    sum_list[i] = nums[i-1] + sum_list[i-1]

for _ in range(m):
    i, j = map(int, input().split())
    print(sum_list[j] - sum_list[i-1])