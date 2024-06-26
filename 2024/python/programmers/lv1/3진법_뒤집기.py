def solution(n):
    # 1. 3진법으로
    nums = ''
    while n > 0:
        nums = str(n % 3) + nums
        n //= 3

    # 2. 10진법으로
    ans = 0
    # ans = int(nums, 3) # 문자열을 3진수로 변경
    for i in range(len(nums)): # 뒤집지 않아서 인덱스 그대로 사용
        ans += (int(nums[i]) * (3 ** i))

    return ans