import sys
n = int(input())

stations = []
for _ in range(n):
    a, b = map(int, input().split())
    stations.append((a,b))

stations.sort(key = lambda x:x[1])
print(*stations[0])