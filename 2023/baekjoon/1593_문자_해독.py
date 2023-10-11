from itertools import permutations
# g: 찾고자 하는 단어의 길이
# s: 벽화에서 추출한 문자열의 길이
g, len_s = map(int, input().split())
# 찾고자 하는 단어
w = input()
# 벽화 속 문자열
s = input()

# 대소문자 구별
# w 의 순열이 s 안에 있을 수 있는 형태의 개수

# g의 모든 조합 확인

# 슬라이딩 윈도우 사용
# 윈도우를 이동시키며 첫 문자를 빼고, 뒷 문자를 넣는 식으로 진행

answer = 0
# 등장한 문자의 개수를 카운드
wa = [0] * 58
sa = [0] * 58

for x in w:
    wa[ord(x) - 65] += 1 # 아스키코드로 변환

start, length = 0, 0
for i in range(len_s):
    # s 개수 카운트
    sa[ord(s[i]) - 65] += 1
    length += 1

    if length == g:
        if wa == sa: # 순서 상관 없이 들어있기만 하면 되니깐...!
            answer += 1
        # 시간 복잡도 줄이기
        # 매번 sa 배열을 작성하는 것이 아니라
        # 처음 값 빼고, 나중 값 넣는 식으로 갱신
        sa[ord(s[start]) - 65] -= 1
        start += 1
        length -= 1
print(answer)
'''
# 시간 초과
per = list(permutations(w, g))

per_list = []
for p in per:
    p = ''.join(p)
    per_list.append(p)

ans = 0

for char in per_list:
    if char in s:
        ans += 1

print(ans, end='') 
'''
