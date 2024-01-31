import sys

w, n = map(int, input().split())
jw = []
for _ in range(n):
    m, p = map(int, input().split())
    jw.append((m, p))
jw.sort(reverse=True, key=lambda x: x[1])
coin = 0

for m, p in jw:
    if m <= w:
        w -= m
        coin += (p * m)
    else:
        coin += (w * p)
        break

print(coin)