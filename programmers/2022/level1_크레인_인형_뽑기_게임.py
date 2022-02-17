def solution(board, moves):
    doll = board
    num = 0 # 배열의 크기를 담음
    box = [] # 뽑은 인형을 담음
    answer = 0

    # 배열의 크기 세기
    for _ in board[0]:
        num += 1
    for i in moves:
        for j in range(num):
            if (doll[j][i-1] != 0): # 행과 열을 바꾸어 작성하지 않도록 주의
                box.append(doll[j][i-1])
                doll[j][i-1] = 0
                if(len(box) > 1):
                    if(box[len(box)-1] == box[len(box) - 2]):
                        answer += 2
                        box.pop()
                        box.pop()
                break
            else:
                continue
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))
