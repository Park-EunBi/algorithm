import sys
n = int(input())
soil = list(map(int, input().split()))

ret = -9999999
for i in range(n - 1):
    for j in range(i + 1, n):
        ret = max(ret, soil[i] * soil[j])

print(ret)