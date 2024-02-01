import sys
n, m = map(int, input().split())

limit = [0] * 101
now = 1

for _ in range(n):
    meter, speed = map(int, input().split())
    for i in range(now, now + meter):
        limit[i] = speed

    now += meter

ret = 0
now = 1
for _ in range(m):
    meter, speed = map(int, input().split())
    for i in range(now, now + meter):
        ret = max(ret, speed - limit[i])
    now += meter

print(ret)