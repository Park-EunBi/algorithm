# n이 1이 될 때 까지 두 과정 중 하나 반복 실행
# 1. n -= 1
# 2. n //= k ( n % k == 0 일 때만 가능)
# 두 과정을 반복하며 1을만드는 최소 횟수 구하기

# n: 17, k: 4
# 17 -1 -> 16 // 4 -> 4 // 4 -> 1 : 3번

n, k = map(int, input().split())

result = 0

''' 
<나의 풀이>
n 이 1이 될 때까지
0으로 나눠지면 1번
아니라면 2번 수행

이렇게 된다면 100억이 넘어가는 수가 들어왔을 땐 시간 초과 

<code>
while (n > 1):
    if n % k == 0:
        n //= k
    else:
        n -= 1
    result += 1

print(result)
'''

# <다른 풀이>
# 몫을 기준으로 계속 나눠가고
# 나머지 만큼 더하면 된다

while 1:
    target = (n//k) * k
    result += (n - target)
    n = target

    if n < k:
        break
    result += 1
    n //= k

print(result)


'''
<testCase>
25 5 
<answer> 
2

<testCase>
17 4
<answer>
3
'''
