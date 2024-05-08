n = int(input())
li = list(map(int, input().split()))

tb = [True for _ in range(1001)]

tb[0], tb[1] = False, False

for i in range(2, 1001):
    if tb[i]:
        for j in range(i*2, 1001, i):
            tb[j] = False

cnt = 0
for l in li:
    if tb[l]:
        cnt += 1

print(cnt)