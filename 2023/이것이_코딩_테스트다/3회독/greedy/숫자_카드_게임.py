# 가장 높은 숫자가 쓰인 카드 한 장 뽑기
# N: 행, M: 열
# 행 선택 후 행에서 가장 작은 수를 뽑아야 한다

n, m = map(int, input().split())
cards = []
for i in range(n):
    cards.append(list(map(int, input().split())))
    cards[i].sort()
cards.sort(reverse=True)
print(cards[0][0])