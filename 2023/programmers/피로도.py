from itertools import permutations
def solution(k, dungeons):
    answer = 0

    # 모든 경우를 다 돌아본다
    for p in permutations(dungeons, len(dungeons)):
        tmp = k
        cnt = 0

        for need, minus in p:
            if tmp >= need:
                tmp -= minus
                cnt += 1
        # 현재 구한 값과 이전에 구한 가장 큰 값 중 큰 값을 저장
        answer = max(cnt, answer)
    return answer