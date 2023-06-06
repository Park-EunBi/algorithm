import heapq # 우선순위 큐

n = int(input())
cards = []
for _ in range(n):
    # cards.append(int(input()))
    # 우선순위 큐에 삽입
    heapq.heappush(cards, int(input()))

result = 0

# 큐에 값이 없을 때 까지
while len(cards) != 1:
    one = heapq.heappop(cards)
    two = heapq.heappop(cards)

    # 합쳐서 다시 정렬
    temp = one+ two
    result += temp
    heapq.heappush(cards, temp)

print(result)

'''
<testCase>
3
10
20
40

<answer>
100
'''