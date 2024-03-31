import heapq
import sys
input = sys.stdin.readline

n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]

times.sort(key = lambda x: (x[0], x[1]))

# 연속으로 사용할 수 없는 강의의 종료 시간 등록
h = [times[0][1]] # 종료 시간 등록

for i in range(1, n):
    # 연속 배정 가능
    if times[i][0] >= h[0]:
        heapq.heappop(h)
    heapq.heappush(h, times[i][1])

print(len(h))