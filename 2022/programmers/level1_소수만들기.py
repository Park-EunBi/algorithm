def solution(nums):
    num = 0
    answer = 0
    # 3개의 숫자 선택하기
    for i in range(len(nums) -2):
        for j in range(i + 1, len(nums)-1):
            for k in range(j + 1, len(nums)):
                num = nums[i] + nums[j] + nums[k]
                # 소수 판단하기
                # 약수가 1과 자기자신 밖에 없는 수
                for a in range(2, num):
                    if (num % a == 0):
                        break
                    else:
                        if (a + 1 == num):
                            answer += 1
                            continue

    return answer

print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))

'''
from itertools import combinations 
    # combinations: 배열의 모든 조합 만들기
    for a in combinations(nums, 3):
    '''
