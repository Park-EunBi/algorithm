# 가장 '높은' 숫자가 쓰인 카드 한장 뽑기
# n: 행, m: 열
# n 선택 -> 해당 행에 포함된 카드 중 가장 '작은' 카드

n, m = map(int, input().split())
cards = []
smallCard = []
for i in range(n):
    cards.append(list(map(int, input().split())))
    cards[i].sort() # min 함수 사용하면 된다
    smallCard.append(cards[i][0]) # 바로 max 비교하면 된다 

print(max(smallCard))

'''
다른 풀이 
result = 0
for i in range(n):
    cards = list(map(int, input().split()))
    result = max(result, min(cards))

print(result)

'''


'''
<testCase1>
3 3
3 1 2
4 1 4
2 2 2
<answer1>
2

<testCase2>
2 4
7 3 1 8
3 3 3 4
<answer2>
3
'''