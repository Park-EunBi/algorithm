import math
def solution(progresses, speeds):
    day = []
    # 주어진 값을 작업일 배열로 바꾸기
    for idx, p in enumerate(progresses):
        tmp = (100-p) / speeds[idx]
        day.append(math.ceil(tmp))

    # 초기화 코드 위치 주의
    result = []
    res = 0
    big = day[0]
    # big 이 갱신될 때 result 에 append
    for idx, d in enumerate(day):
        if d > big:
            result.append(res)
            big = d
            res = 1
        else:
            res += 1
    # 마지막 값도 추가
    result.append(res)

    return result
print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))