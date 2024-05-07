import sys
import heapq
input = sys.stdin.readline

n = int(input())

# 힙을 두개로 나눔
mn = [] # 작은 값 중 최대 값 비교 - 중앙 값 보다 큰 값 저장
mx = [] # 큰 값 중 작은 값 비교 - 중앙 값 보다 작은 값 저장

for _ in range(n):
    num = int(input())
    if len(mx) == len(mn):
        heapq.heappush(mx, -num) # 최대힙
    else:
        heapq.heappush(mn, num) # 최소힙

    # 최소힙의 최솟값 < 최대힙의 최대값
    if mn and mn[0] < -mx[0]:
        maximum = heapq.heappop(mx)
        minimum = heapq.heappop(mn)
        heapq.heappush(mx, -minimum)
        heapq.heappush(mn, -maximum)

    print(-mx[0])