def solution(n, arr1, arr2):
    # 1: 벽, 0: 공백

    # board = [['0' * n] for _ in range(n)]
    # print(board)

    # 1. 이진수 변환
    def change(num):
        ans = ''
        while num > 0:
            ans = str(num % 2) + ans
            num //= 2

        if len(ans) < n:
            ans = '0' * (n - len(ans)) + ans
        return ans

        # 2. board로 변환

    board1 = []
    for arr in arr1:
        board1.append(change(arr))

    board2 = []
    for arr in arr2:
        board2.append(change(arr))

    # 3. 결과 생성
    answer = []
    for bo1, bo2 in zip(board1, board2):
        tmp = ''
        for b1, b2 in zip(bo1, bo2):
            if int(b1) or int(b2):
                tmp += '#'
            else:
                tmp += ' '

        answer.append(tmp)

    return answer

'''
# sol2)
# 비트 연산 해서 이진수 변환 하면 된다
int(arr1[i]) | int(arr2[i])
'''