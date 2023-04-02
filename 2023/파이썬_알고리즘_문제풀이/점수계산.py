import sys
sys.stdin = open("input.txt", "rt")

# 연속으로 답을 맞출 경우 점수 1점씩 추가
# 3문제 연속으로 맞추면 1 + 2 + 3 점

n = int(input())
answer = list(map(int, input().split()))

score = [0] * (n) # 이 배열 없애고 바로 sum 구하면 된다
cnt = 0 # 몇번 연속된 정답인지 기록

for i in range(n):
    if answer[i] == 1:
        score[i] = cnt + 1 # 배열 안쓰고 score += cnt + 1 해도 된다
        cnt += 1 # 윗 줄과 순서 바꾸면 # score += cnt로 변경 가능
    else:
        cnt=0

print(sum(score))