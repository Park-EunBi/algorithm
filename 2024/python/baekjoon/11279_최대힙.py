import sys
import heapq
input = sys.stdin.readline

n = int(input())
q = []

for _ in range(n):
    num = int(input())
    if num == 0:
        print(-heapq.heappop(q)) if len(q) else print(0)
    else:
        heapq.heappush(q, -num)