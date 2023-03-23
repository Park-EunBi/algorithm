import sys
sys.stdin = open("input.txt", "rt")

n, k = map(int, input().split())

cnt = n % k
while (n > 1):
    n //= k
    cnt += 1

print(cnt)
