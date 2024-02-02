import sys
n = int(input())
houses = list(map(int, input().split()))
houses.sort()

ret = []
for i in range(2, houses[-1] + 1):
    cnt = 0
    for h in houses:
        if h % i == 0:
            cnt += 1
    ret.append(cnt)

print(max(ret))