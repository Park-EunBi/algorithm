import sys
sys.stdin = open("input.txt", "rt")

# n 명의 수학 점수, 학생들의 평균 (소수 첫째자리 반올림)
# 평균에 가장 가까운 학생은 몇번째 학생인지
# 여러 개 일 경우 학생 번호(1부터 시작)가 빠른학생의 번호를 답으로
import math
n = int(input())
scores = list(map(int, input().split()))

avg = round(sum(scores)/n)

sub = abs(scores[0] - avg)
student = 0

for i in range(1, n):
    temp_sub = abs(scores[i] - avg)
    if(temp_sub<sub):
        sub = temp_sub
        student = i + 1
print(avg, student)