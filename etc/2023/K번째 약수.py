import sys
# sys.stdin = open("input.txt", "rt")

n, k = map(int, input().split())

cnt = 0

for i in range(1, n+1):
    if n % i == 0: # n의 약수
        cnt += 1
        if cnt == k: # k 번재 약수 발견
            print(i)
            break
else:
    print(-1)