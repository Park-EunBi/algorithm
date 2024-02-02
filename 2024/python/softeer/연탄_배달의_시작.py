import sys
n = int(input())
houses = list(map(int, input().split()))

d_loc = [0] * 1000001

for i in range(n - 1):
    d_loc[houses[i + 1] - houses[i]] += 1

for loc in d_loc:
    if loc > 0:
        print(loc)
        break

