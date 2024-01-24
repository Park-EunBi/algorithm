import sys
input = sys.stdin.readline

n = int(input())
areas = list(map(int, input().split()))
budget = int(input())

areas.sort()
start, end = 1, max(areas)

while start <= end:
    mid = start + (end - start) // 2
    temp_ret = 0
    for a in areas:
        if a <= mid:
            temp_ret += a
        else:
            temp_ret += mid

    # 이분 탐색
    if temp_ret <= budget: # 부등호 주의
        start = mid + 1
    elif temp_ret > budget:
        end = mid - 1

print(end)
