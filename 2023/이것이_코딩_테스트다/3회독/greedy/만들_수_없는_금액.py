# n 개의 동정
# 동전을 이용하여 만들 수 없는 양의 정수 금액 중 최솟값

n = int(input())
coins = list(map(int, input().split()))

coins.sort()

# 매번 target 금액을 만들 수 있는지 확인
target = 1
for c in coins:
    if target < c:
        break
    else: # 해당 금액을 만들 수 있음
        target += c

print(target)

