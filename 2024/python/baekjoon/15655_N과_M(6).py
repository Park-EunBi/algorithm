n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

choose = []
def choice(start, num):
    if num == m:
        print(*choose)
        return

    for i in range(start, n):
        # if nums[i] not in choose:
        choose.append(nums[i])
        choice(i + 1, num + 1)
        choose.pop()

choice(0, 0)