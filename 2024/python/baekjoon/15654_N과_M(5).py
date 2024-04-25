n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

choose = []
def choice(num):
    if num == m:
        print(*choose)
        return

    for i in nums:
        if i not in choose:
            choose.append(i)
            choice(num + 1)
            choose.pop()

choice(0)