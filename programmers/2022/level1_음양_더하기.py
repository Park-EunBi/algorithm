
def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i] == True:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]

    return answer


# def solution(absolutes, signs):
#
#     for i in range(len(absolutes)):
#         if signs[i] == False:
#             absolutes[i] = absolutes[i]*(-1)
#     return sum(absolutes)

print(solution([4,7,12], [True,False,True]))
print(solution([1,2,3], [False,False,True]))
print(solution([1, 2, 3, 4, 5],[True, False, True, True, False]))
