def solution(k, m, score):
    score.sort(reverse=True)

    ans = 0
    p1, p2 = 0, m - 1 # 시작과 끝 포인터

    for _ in range(len(score) // m):
        ans += (m * score[p2]) # 정렬되어 있기에 p2의 값을 점수로 사용
        # 포인터 이동
        p1 += m
        p2 += m

    return ans

'''
# sol2)
def solution(k, m, score):
    return sum(sorted(score)[len(score)%m::m])*m # 인덱스 뛰어넘기 
'''