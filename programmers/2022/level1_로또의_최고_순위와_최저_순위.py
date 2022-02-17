def solution(lottos, win_nums):
    win = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    cnt = 0  # 맞은 번호 개수
    num_of_0 = lottos.count(0)  # 0의 개수
    result = []

    # 맞은 개수 구하기
    for i in win_nums:
        if i in lottos:
            cnt += 1

    result.append(win[cnt + num_of_0])
    result.append(win[cnt])

    return result


'''
런타임 에러

def solution(lottos, win_nums):
    win = {6: 1, 5: 2, 4: 3, 2: 5, 1:6, 0: 6}

    cnt = 0
    result = []
    #최악의 경우
    for i in range(6):
        for j in range(6):
            if (lottos[i] == win_nums[j]):
                cnt += 1
    result.append(cnt)

#     최고의 경우
    
    for i in range(6):
        if (lottos[i] == 0):
           cnt += 1
    result.append(cnt)
    win_result = []
    win_result.append(win[result[1]])
    win_result.append(win[result[0]])


    return win_result
'''
