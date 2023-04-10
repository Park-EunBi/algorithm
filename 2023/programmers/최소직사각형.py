def solution(sizes):
    # [0] > [1] 이 되도록 정렬하기
    for s in sizes:
        if s[0] < s[1]:
            s[0], s[1] = s[1], s[0]

    # [0], [1] 에서 각각 가장 큰 값 answer 에 곱해주기
    maximum_0 = 0
    maximum_1 = 0
    for s in sizes:
        if s[0] > maximum_0:
            maximum_0 = s[0]

        if s[1] > maximum_1:
            maximum_1 = s[1]

    return maximum_0 * maximum_1

# print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
# print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
# print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))

'''
# 코드 최적화 

def solution(sizes):
    row = 0
    col = 0
    for a, b in sizes:
        if a < b:
            a, b = b, a
        row = max(row, a)
        col = max(col, b)
    return row * col

'''