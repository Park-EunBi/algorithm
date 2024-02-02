import sys

n = int(input())
for _ in range(n):
    a, b = input().split()
    a = a.upper()
    b = b.upper()

    idx = a.index('X')
    print(b[idx], end='')