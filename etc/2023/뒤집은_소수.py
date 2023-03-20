import sys
sys.stdin = open("input.txt", "rt")

# n 개의 자연수를 뒤집은 후 뒤집은 수가 소수이면 출력
# 32 -> 23: 23은 소수
# 910 -> 19
# def reverse (x), def isPrime(x) 필수

def reverse(x):
    x = list(str(x))
    x = int(''.join(x[::-1]))
    # print(x)
    return x

def isPrime(x):
    x = reverse(x)
    if x == 1:
        return False
    # if x == 2:
    #     return x
    for i in range(2, x): # 소수는 절반까지만 존재하게 되므로
        # range(2, x//2 + 1)으로 해도 무방하다
        if x % i == 0:
            return False
    return x


n = int(input())
nums = list(map(int, input().split()))
for num in nums:
    res = isPrime(num)
    if res:
        print(res, end=" ")


'''
# 다른 풀이 
def reverse(x):
    res = 0
    while > 0:
        t = x % 10
        res = res * 10 + t
        x = x // 10
    return res 
'''