# https://www.codetree.ai/missions/2/problems/n-permutations-of-k-with-repetition?&utm_source=clipboard&utm_medium=text

k, n = map(int, input().split())

answer = []

def print_answer():
    for a in answer:
        print(a, end=' ')
    print()

def solution(now):
    # 재귀 종료 조건
    if now == n + 1:
        print_answer()
        return

    # 모든 수를 뽑아야 하므로
    for i in range(1, k + 1):
        answer.append(i)
        solution(now + 1)
        answer.pop()

solution(1)
