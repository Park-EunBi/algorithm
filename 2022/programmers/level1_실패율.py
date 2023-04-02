def solution(N, stages):
    People = len(stages)
    faillist = {}
    for i in range(1, N + 1):
        if People != 0:
            faillist[i] = stages.count(i) / People
            People -= stages.count(i)
        else:
            faillist[i] = 0

    return sorted(faillist, key=lambda i: faillist[i], reverse=True)


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4,4,4,4]))

'''
import collections
def solution(N, stages):
    # 빈도수 계산
    fail = collections.Counter(stages)
    player = []

    # list에 현재 통과 못한 사람 수 등록
    for i in range(max(stages)):
        if i+1 in fail.keys():
            player.insert(i, fail[i+1])
        else:
            player.insert(i, 0)

    # list에 현재 단계를 지난 사람 등록
    for i in range(len(player)):
        for j in range(len(player)):
            if i < j:
                player[i] += player[j]

    answer = []
    # 실패율 계산
    result = []
    for i in range(len(player)):
        result.insert(i, fail[i+1]/player[i])
    find_index = []
    find_index = result.copy()
    result.sort(reverse=True)
    for i in range(len(result)):
        answer.append(find_index.index(result[i]) + 1)

    return answer
'''

