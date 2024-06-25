def solution(n):
    nums = [0 for _ in range(n + 1)]  # 1 - 소수 x

    for i in range(2, n + 1):
        for j in range(i * 2, n + 1, i):
            nums[j] = 1

    return sum([
        1
        for i in range(2, n + 1)
        if not nums[i]
    ])

'''
# sol2)
def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)
'''