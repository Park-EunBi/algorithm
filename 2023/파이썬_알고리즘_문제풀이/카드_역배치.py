import sys
sys.stdin = open("input.txt", "rt")

# 1~20 적힌 20장의 카드가 오름차순으로 나열
# [a, b] 구간: 카드를 현재의 역순으로 나열
# 오름차순으로 놓여있는 20장의 카드에 대해 10개구간이 주어짐
# 마지막 카드들의 배치를 구하기

# 카드 초기화
cards = list(range(21))
# print(cards)

for i in range(10):
    a, b = map(int, input().split())
    for j in range(a, (b-a) // 2 + a):
        tmp = cards[b + a -j]
        cards[b + a -j] = cards[j]
        cards[j] = tmp
        print(cards)

for i in range(1, len(cards)):
    print(cards[i], end=" ")

