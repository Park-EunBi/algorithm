import sys
sys.stdin = open("input.txt", "rt")

# 원소의 개수가 n개인 두 배열 a, b
# 최대 k번 동안
# 배열 a와 b의 원소를 바꾸는 것
# 목표: 배열 a의 모든 원소의 합이 최대가 되도록
# 배열 a의 모든 원소의 합의 최댓값을 출력

n, k = map(int, input().split())
A = (list(map(int, input().split())))
B = (list(map(int, input().split())))

A.sort()
B.sort(reverse=True)
for i in range(k):
    if A[i] < B[i]:
        A[i] = B[i]
    else:
        break
print(sum(A))