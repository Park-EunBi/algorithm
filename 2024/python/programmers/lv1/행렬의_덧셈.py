def solution(arr1, arr2):
    n = len(arr1)
    m = len(arr1[0])
    answer = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            answer[i][j] = arr1[i][j] + arr2[i][j]

    return answer

c
'''
# sol2)
def solution(arr1, arr2):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(arr1, arr2)]
    return answer
'''