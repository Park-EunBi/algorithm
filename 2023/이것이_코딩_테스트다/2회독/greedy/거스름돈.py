'''
이코테 예제
'''
# 거스름돈 500, 100, 50, 10
# 거슬러 줘야 할 돈 N (10의 배수)
# 거슬러 줘야 하는 동전의 최소 개수

n = 1260

count = 0
coins = [500, 100, 50, 10]

# 1260 // 500 : 2
# 1260 % 500 : 260

# for i in range(4)
for c in coins:
    count += (n // c)
    n %= c

print(count)

'''
백준 5585 거스름돈
'''
money = int(input())
money = 1000 - money

coins = [500, 100, 50, 10, 5, 1]
count = 0

# 1260 // 500 : 2
# 1260 % 500 : 260
for c in coins:
    count += (money // c)
    money %= c

print(count)
