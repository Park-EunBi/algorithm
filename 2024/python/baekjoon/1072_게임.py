x, y = map(int, input().split())
# (y//x) * 100: 부동 소수점 오류
z = (100 * y) // x

# 이분 탐색
left, right, ret = 0, x, x # 최대: x
if z >= 99: # 더이상 증가 할 수 없음
    print(-1)
else:
    while left <= right:
        mid = (left + right) // 2
        nz = (100 * (y + mid)) // (x + mid) # 새로운 승률
        if nz > z:
            ret = mid
            right = mid - 1
        else:
            left = mid + 1

    print(ret)