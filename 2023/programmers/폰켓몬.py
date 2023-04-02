def solution(nums):
    answer = 0
    # 해시 테이블 생성
    pon = {}
    for n in nums:
        if n not in pon:
            pon[n] = 1
        else:
            pon[n] += 1

    get_pon = len(nums)//2
    num_pon = len(pon)
    # 폰켓몬의 종류 >= n//2 이면 n//2 리턴
    if num_pon >= get_pon:
        return get_pon
    # 폰켄몬의 종류 < n//2 이면 폰켓몬의 종류 리턴
    else:
        return num_pon

    return answer

print(solution([3,1,2,3])) # 2
print(solution([3,3,3,2,2,4])) # 3
print(solution([3,3,3,2,2,2])) # 2