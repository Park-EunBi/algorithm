import sys
from collections import deque
input = sys.stdin.readline

s, p = map(int, input().split()) # 문자열 길이, 부분 문자열 길이
dna = list(input())
include = list(map(int, input().split()))

# 부분 문자열의 최소 크기 : sum(include)
length = sum(include)

start = 0
end = p - 1
ans = 0

arr = deque(dna[start:end])

hash = {
    'A': 0,
    'C': 0,
    'G': 0,
    'T': 0
}

for a in arr:
    hash[a] += 1

while end < s:
    # 오른쪽 문자 추가
    hash[dna[end]] += 1

    # 검사
    if hash['A'] >= include[0] and hash['C'] >= include[1] and hash['G'] >= include[2] and hash['T'] >= include[3]:
        ans += 1

    # 이동
    hash[dna[start]] -= 1
    start += 1
    end += 1

print(ans)