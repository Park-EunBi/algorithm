import sys

ret = 0

for _ in range(5):
    start, end = input().split()
    start_h = int(start[:2])
    start_m = int(start[3:5])
    end_h = int(end[:2])
    end_m = int(end[3:5])

    ret += (end_h - start_h) * 60
    ret += end_m - start_m

print(ret)