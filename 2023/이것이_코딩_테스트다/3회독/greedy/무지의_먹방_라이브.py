# https://school.programmers.co.kr/learn/courses/30/lessons/42891
# 시간이 적게 걸리는 음식 부터 계산해나가기
# 테트리스 처럼 한 번에 제거 가능
# 우선순위 큐 사용

import heapq

def solution(food_times, k):
    # 전체 음식을 먹는 시간이 k 보다 크다면
    # 네트워크 정지 시간 동안 음식을 다 먹어 더이상 먹을 음식이 없음 => -1 반환
    if sum(food_times) <= k:
        return -1

    # 시간이 적게 걸리는 음식 부터 빼나가야 하므로 우선순위 큐 사용
    q = []
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i + 1))

    sum_value = 0 # 먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 시간
    length= len(food_times) # 남은 음식의 개수

    # sum_value + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수 와 k 비교
    # sum_value 는 누적 값
    # {(현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수}는 한 번에 빼 줄 시간
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1 # 다 먹은 음식 제외
        previous = now # 이전 음식 시간 재설정

    # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    result = sorted(q, key=lambda x:x[1])
    return result[(k-sum_value) % length][1]