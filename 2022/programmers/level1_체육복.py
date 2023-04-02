def solution(n, lost, reserve):
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)
    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i - 1)
        elif i+1 in set_lost:
            set_lost.remove(i + 1)
    return n-len(set_lost)

'''
틀린 이유 파악 중 
    answer = n - len(lost)

    for i in range(len(lost)):
        if lost[i] in reserve:
            reserve.remove(lost[i])
            lost.remove(lost[i])
            answer -= 1

        if lost[i] + 1 <= n:
            if lost[i] + 1 in reserve:
                answer += 1
                reserve.remove(lost[i] + 1)
                # print(reserve)

        elif lost[i] -1 >= 1:
            if lost[i] - 1 in reserve:
                answer += 1
                reserve.remove(lost[i] - 1)
                # print(reserve)

    return answer
'''

print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))
