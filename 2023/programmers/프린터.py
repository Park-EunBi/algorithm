from collections import deque
def solution(priorities, location):
    result = 0
    # 큐 만들기
    d = deque([(v, i) for i, v in enumerate(priorities)])

    while (d):
        # 가장 앞에 있는 문서 빼내기
        item = d.popleft()
        # 나머지 대기 목록과 빼낸 문서 중 큰 값 비교
        if d and max(d)[0] > item[0]:
            d.append(item)
        else:
            result += 1
            # 확인을 원하는 문서의 출력 위치 확인
            if item[1] == location:
                return result

# print(solution([2, 1, 3, 2], 2))
# print(solution([1, 1, 9, 1, 1, 1], 0))