n, m = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
coins.sort()
cnt = 0
res = m
for i in range(m, 0, -1):
    for j in range(n):
        if res % coins[j] == 0:
            res //= coins[j]
            cnt += 1
        else:
            res -= 1

print(cnt)