import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 포켓몬 수, 문제 개수

# 1. 도감 완성
pockets = [input().rstrip() for _ in range(n)]
pockets.insert(0, '')

# 1-1. 해시 변환
hash = {}
for idx, p in enumerate(pockets):
    hash[p] = idx

# 2. 문제 입력
for _ in range(m):
    q = input().rstrip()
    if q.isalpha():
        print(hash[q])
    else:
        print(pockets[int(q)])
