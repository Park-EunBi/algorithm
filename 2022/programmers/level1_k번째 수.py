def solution(array, commands):
    answer = []
    for com in commands:
        # sort = sorted(array[com[0]-1:com[1]])
        # answer.append(sort[com[2]-1])
        answer.append(sorted(array[com[0] - 1:com[1]])[com[2]-1])
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
'''
[다른 풀이]

    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
'''