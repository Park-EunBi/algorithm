# n 개의 동전
# n 개의 동전을 사용하여 만들 수 없는 양의 정수 금액 중 최솟값

# n = 5, 화폐단위: 3, 2, 1, 1, 9

n = int(input())
coins = list(map(int, input().split()))
coins.sort()

target = 1
for c in coins:
    if target < c:
        break
    # target 이하의 값은 모두 만들 수 있다
    target += c

print(target)

'''
<testCase>
5
3 2 1 1 9
<answer>
8
'''