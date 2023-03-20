import sys
sys.stdin = open("input.txt", "rt")

# n 명의 수학 점수, 학생들의 평균 (소수 첫째자리 반올림)
# 평균에 가장 가까운 학생은 몇번째 학생인지
# 여러 개 일 경우 학생 번호(1부터 시작)가 빠른학생의 번호를 답으로
import math
n = int(input())
scores = list(map(int, input().split()))

# avg = round(sum(scores)/n)
# round는 round_half_even 방식을 사용
    # 정확하게 반으로 되었을 때 짝수 값으로 근사함
    # round(4.500) # 4
    # round(4.511) # 5
    # round(5.500) # 6
avg = sum(scores)/n + 0.5
avg = int (avg)

sub = abs(scores[0] - avg) # == min = 2147000000
student = 0

for i in range(1, n): # for idx, x in enumerate(a):
    temp_sub = abs(scores[i] - avg)
    if(temp_sub<sub):
        sub = temp_sub
        student = i + 1
print(avg, student)

'''
# 정답 풀이 
for idx, x in enumerate(a):
    tmp = abs(x - avg)
    if tmp < sub:
        sub = tmp
        score = x
        res = idx + 1
    elif tmp == sub:
        if x > score:
            score = x
            res = idx + 1
'''