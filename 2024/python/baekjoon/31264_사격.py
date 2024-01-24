'''
틀림... 정답 코드 못찾음
'''
import sys
input = sys.stdin.readline

n, m, a = map(int, input().split())
targets = set(map(int, input().split()))
targets = sorted(targets)
# targets = sorted(targets, reverse = True)
# targets.sort(reverse = True)
# print(targets)

def shooting(init_skill):
    skill = init_skill
    score = 0

    for _ in range(m):
        # 이분 탐색으로 변경 - 틀림
        # 맞힐 수 있는 표적 중 점수가 가장 높은 것
        start, end = 0, len(targets) - 1
        while start <= end:
            mid = start + (end - start) // 2
            # print(start, end, mid, targets[mid])
            if targets[mid] < skill:
                start = mid + 1
            elif targets[mid] > skill:
                end = mid - 1
            else:
                break
        skill += targets[end]
        score += targets[end]
        # print()

        '''
        # 시간 초과 
        for target in targets:
            if target <= skill:
                skill += target
                score += target
                break
        '''
    return score

start, end = 1, 10 ** 10
while start <= end:
    mid = start + (end - start) // 2
    check_score = shooting(mid)
    if check_score < a: # 목표 점수에 도달하지 못하면
        start = mid + 1
    elif check_score > a:
        end = mid - 1

print(start)