# n 에서 1 빼기
# n을 k로 나누기
# 위의 연산을 수행하여 n을 1로 만드는 최소 연산 횟수 구하기

n, k = map(int, input().split())

cnt = 0

while n > 1:
    if n % k == 0:
        n //= k
    else:
        n -= 1
    cnt += 1

print(cnt)


'''
# 100억 이상의 값이 들어왔을 경우 
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