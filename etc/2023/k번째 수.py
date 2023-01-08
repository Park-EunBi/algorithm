import sys
# sys.stdin = open("input.txt", "rt")

t = int(input())
for i in range(t):
    n, s, e, k = map(int, input().split())
    nums = list(map(int, input().split()))

    nums = nums[s-1: e]
    nums.sort()
    print("#%d %d" %(i + 1, nums[k-1]))

