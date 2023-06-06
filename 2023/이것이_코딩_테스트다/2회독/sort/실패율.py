def solution(N, stages):
    answer = [] # 실패율 계산
    result = {} # 실패율 인덱스, 값 -> dict으로 저장 (정렬한 뒤 인덱스 반환해야 해서)
    # round
    for i in range(1, N + 1):
        pass_stage = 0 # 해당 스테이지를 넘어간 사람들 (스테이지에 도달한 플레이어 수)
        now_stage = 0  # 현재 해당 라운드에 도달한 사람의 수 (스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수)

        for s in stages:
            if i <= s:
                pass_stage += 1
            if i == s:
                now_stage += 1

        # 0으로 나누면 런타임 오류
        if pass_stage == 0:
            answer.append(0)
        else:
            answer.append(now_stage / pass_stage)

    # 인덱스와 값 dict 에 저장
    for idx, a in enumerate(answer):
        result[idx] = a
    # value 기준으로 내림차순 정렬
    result = sorted(result.items(), key=lambda x: x[1], reverse=True)
    # result 에 index 값만 저장 (반환용)
    result = [x[0] + 1 for x in result]

    return result