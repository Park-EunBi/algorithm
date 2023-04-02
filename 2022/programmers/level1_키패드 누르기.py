def solution(numbers, hand):
    answer = ''
    key = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    left = [1, 4, 7, '*']
    right = [3, 6, 9, "#"]
    last_left = '*' #왼손의 마지막 위치 저장
    last_right = '#'
    for i in numbers:
        if(i in left):
           answer = answer + "L"
           last_left = i
        elif(i in right):
            answer = answer + "R"
            last_right = i
        else:
            #마지막 왼손의 위치와 i 위치를 비교
            #마지막 오른손의 위치와 i 위치를 비교
            #둘의 차이 중 작은 값 저장하고 손의 위치를 변경

        # 계산한 거리차 담는 곳
            l_dis = 99
            r_dis = 99

            for k in range(4):
                for j in range(3):
                    if key[k][j] == i:

                        # 왼쪽 손의 좌표
                        for l_row in range(4):
                            for l_col in range(3):
                                if (key[l_row][l_col] == last_left):
                                    l_dis = abs(k-l_row) + abs(j-l_col)


                        # 오른 손의 좌표
                        for r_row in range(4):
                            for r_col in range(3):
                                if (key[r_row][r_col] == last_right):
                                    r_dis = abs(k-r_row) + abs(j-r_col)

                        if(l_dis < r_dis):
                            answer = answer + "L"
                            last_left = i
                        elif(l_dis > r_dis):
                            answer = answer + "R"
                            last_right = i
                        else:
                            if(hand == "left"):
                                answer = answer + "L"
                                last_left = i
                            else:
                                answer = answer + "R"
                                last_right = i


    return answer

'''

0,0 0,1 0,2
1,0 1,1 1,2
2,0 2,1 2,2
3,0 3,1 3,2

두 좌표에서 행끼리, 열끼리 값 빼서 더하면 거리 값 나옴 
'''


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
if(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right") == "LRLLLRLLRRL"):
    print(True)

print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
if(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left") == "LRLLRRLLLRR"):
    print(True)

print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))
if(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right") == "LLRLLRLLRL"):
    print(True)

'''
시도했던 풀이 방법 
-숫자 차이와 거리차의 관계를 파악해보려 함
-규칙을 파악하지 못해 다른 방식으로 시도

0를 주의 
손이 *, #에 있을 때 주의
왼쪽 
    차이가 1이면 거리가 1
    차이가 2이면 거리가 2
    차이가 4이면 거리가 2
    차이가 5이면 거리가 3
    차이가 7이면 거리가 3

오른쪽 
    차이가 1이면 거리가 1
    차이가 2이면 거리가 2
    차이가 4이면 거리가 3
    차이가 5이면 거리가 3
    ...
  
'''
