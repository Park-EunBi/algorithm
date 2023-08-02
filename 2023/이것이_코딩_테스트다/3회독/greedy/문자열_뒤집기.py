# https://www.acmicpc.net/problem/1439
# 0 -> 1, 1 -> 0 으로 뒤집어 모두 같은 수로 만들기
# 행동의 최소 횟수 구하기

s = list(map(int, input()))

turn_zero = 0
turn_one = 0

if s[0] == 0:
    turn_one += 1
else:
    turn_zero += 1

for i in range(len(s)-1): # 두 글자씩 비교할거라
    if s[i] == 0 and s[i + 1] == 1:
        turn_zero += 1
    elif s[i] == 1 and s[i + 1] == 0:
        turn_one += 1

print(min(turn_zero, turn_one))
