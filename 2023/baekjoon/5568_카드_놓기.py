from itertools import combinations
from itertools import permutations

n = int(input()) # 카드의 개수 (4 <= n <= 10)
k = int(input()) # 선택할 카드의 수
cards = [
    # int(input())
    input()
    for _ in range(n)
]
# 1. n장의 카드 중 k 개의 카드 선택 - combinations
# select_cards = map(list, combinations(cards, k))
select_cards = list(map(list, combinations(cards, k)))
make_nums = []

# 2. 각 조합을 permutaion 해서 문자로 만들기
for cards in select_cards:
    nums = list(map(list,permutations(cards, k)))
    for num in nums:
        make_nums.append(''.join(num))

make_nums = set(make_nums)
print(len(make_nums))