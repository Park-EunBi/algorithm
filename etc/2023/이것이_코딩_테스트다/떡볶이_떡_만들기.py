import sys
sys.stdin = open("input.txt", "rt")

n, m = map(int,input().split()) # m : 요청한 떡의 길이
rice_cake = list(map(int, input().split()))

start = 0
end = max(rice_cake)

# 이진 탐색 수행 (0 ~ 떡의 최대 길이)
result = 0
while (start <= end):
    total = 0
    mid = (start + end) // 2

    for x in rice_cake:
        # 잘랐을 때 떡의 양 계산
        if x > mid:
            total += x - mid
    # 양이 부족한 경우 더 많이 짜르기 (왼쪽)
    if total < m:
        end = mid -1
    # 양이 충분한 경우 덜 짜르기 (오른쪽)
    else:
        result = mid
        start = mid + 1

print(result)