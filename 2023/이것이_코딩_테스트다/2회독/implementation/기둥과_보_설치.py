# 현재 구조로 설치 가능한지 확인하는 함수
def possible(answer):
    for x, y, stuff in answer:
        # 기둥이면
        if stuff == 0:
            # 바닥 위, 보의 한쪽 끝 위, 다른 기둥 위 -> 가능
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False

            # 보 인경우
        elif stuff == 1:
            # 한쪽 끝이 기중 위, 양쪽 끝부분이 다른 보와 동시에 연결 -> 가능
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or (
                    [x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        # 작업 받아오기
        x, y, stuff, operate = frame
        # 삭제
        if operate == 0:
            # 삭제
            answer.remove([x, y, stuff])
            # 구조 확인
            if not possible(answer):
                # 불가능하면 다시 설치
                answer.append([x, y, stuff])

        # 설치
        if operate == 1:
            answer.append([x, y, stuff])
            if not possible(answer):
                answer.remove([x, y, stuff])
    return sorted(answer)

print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))