# https://www.codetree.ai/missions/2/problems/conveyor-belt-triangle?utm_source=clipboard&utm_medium=text

n, t = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

nums = a + b + c

for _ in range(t):
    temp = nums[-1]
    for i in range(3 * n - 1, 0, -1):
        nums[i] = nums[i - 1]
    nums[0] = temp

for num in nums[:n]:
    print(num, end = ' ')
print()

for num in nums[n:2 * n]:
    print(num, end=' ')
print()

for num in nums[2*n:]:
    print(num, end = ' ')