import sys
sys.stdin = open("input.txt", "rt")

# 1 ~ 100 사이의 n장의 카드 중복 가능
# 3장을 뽑아 카드에 적힌 수 기록
# 3장을 뽑을 수 있는 경우 모두 기록, k번째로 큰 수 출력
# k-1

n, k = map(int, input().split())
cards = list(map(int, input().split()))

# 중복을 제거하는 것이 중요 -> set
sums = set()
# 중복해서 3개 뽑는 모든 경우의 수 더하기
for i in range(n): # 첫번째 뽑기
    for j in range(i + 1, n): # 두번째 뽑기, 중복을 방지하기 위해 i + 1
        for m in range(j+1,n): # 세번째 뽑기, k 이미 사용했으니 주의, 중복을 방지하기 위해 j + 1
            sums.add(cards[i] + cards[j] + cards[m])

sums = list(sums) # set은 sort 기능이 없음
sums.sort(reverse=True)
print(sums[k-1])